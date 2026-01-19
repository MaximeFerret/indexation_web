from typing import Dict, List
import nltk
from nltk.corpus import stopwords

from search_engine.loader import load_json, load_jsonl
from search_engine.persistence import load_index
from search_engine.query import parse_query
from search_engine.query_expansion import expand_query_with_synonyms
from search_engine.filtering import (
    filter_documents_all_tokens,
    filter_documents_any_token
)
from search_engine.ranking.bm25 import compute_bm25_score
from search_engine.ranking.exact_match import compute_exact_match_score
from search_engine.ranking.linear_scorer import compute_linear_score
from search_engine.spell_correction import correct_tokens

def search(query: str, input_dir: str = "input") -> Dict:
    """
    Executes a search query and returns ranked results.
    
    Parameters
    ----------
    query: str
        The user's query
    input_dir: str
        The imput directory path
        
    Return
    ------
    Dict
        The query results
    """

    # LOAD
    nltk.download("stopwords", quiet=True)
    stop_words = set(stopwords.words("english"))

    title_index = load_index(f"{input_dir}/title_index.json")
    description_index = load_index(f"{input_dir}/description_index.json")
    brand_index = load_index(f"{input_dir}/brand_index.json")
    origin_index = load_index(f"{input_dir}/origin_index.json")
    reviews_index = load_index(f"{input_dir}/reviews_index.json")

    vocabulary = set(title_index.keys()) | set(description_index.keys())

    synonyms = load_json(f"{input_dir}/origin_synonyms.json")
    products = load_jsonl(f"{input_dir}/rearranged_products.jsonl")

    indexes = {
        "title": title_index,
        "description": description_index,
        "brand": brand_index,
        "origin": origin_index
    }


    # QUERY PROCESSING
    tokens = parse_query(query, stop_words)
    tokens = correct_tokens(tokens, vocabulary)
    expanded_tokens = expand_query_with_synonyms(tokens, synonyms)

    # Keep only the k=5 rarest words (manage long queries)
    expanded_tokens = sorted(
        expanded_tokens,
        key=lambda t: len(title_index.get(t, []))
    )[:5]

    # Ignore unknown words
    expanded_tokens = [
        t for t in expanded_tokens
        if t in title_index or t in description_index
    ]


    # FILTERING
    candidate_docs = filter_documents_any_token(expanded_tokens, indexes)
    filtered_docs = filter_documents_all_tokens(expanded_tokens, indexes, stop_words)

    if filtered_docs:
        candidate_docs = filtered_docs

    # RANKING
    results = []
    doc_lengths = {
        url: sum(
            len(title_index.get(token, {}).get(url, []))
            for token in title_index
        )
        for url in candidate_docs
    }


    avg_doc_length = (
        sum(doc_lengths.values()) / len(doc_lengths)
        if doc_lengths else 1
    )

    for document in products:
        url = document.get("url")
        if url not in candidate_docs:
            continue

        title = document.get("title", "")
        description = document.get("description", "")

        bm25_title = compute_bm25_score(
            url,
            expanded_tokens,
            title_index,
            avg_doc_length,
            doc_lengths
        )

        bm25_description = compute_bm25_score(
            url,
            expanded_tokens,
            description_index,
            avg_doc_length,
            doc_lengths
        )

        exact_match = compute_exact_match_score(
            title,
            description,
            query
        )

        review_data = reviews_index.get(url, {})
        mean_mark = review_data.get("mean_mark", 0)
        total_reviews = review_data.get("total_reviews", 0)

        features = {
            "bm25_title": bm25_title,
            "bm25_description": bm25_description,
            "exact_match": exact_match,
            "mean_mark": mean_mark,
            "total_reviews": total_reviews
        }

        # Weights fixed arbitrarily
        weights = {
            "bm25_title": 2.0,
            "bm25_description": 1.0,
            "exact_match": 3.0,
            "mean_mark": 0.5,
            "total_reviews": 0.1
        }
        
        final_score = compute_linear_score(features, weights)

        results.append({
            "title": title,
            "url": url,
            "description": description,
            "score": round(final_score, 4),
            "metadata": {
                "reviews": review_data
            }
        })

    # SORT
    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "query": query,
        "total_documents": len(products),
        "filtered_documents": len(candidate_docs),
        "results": results
    }