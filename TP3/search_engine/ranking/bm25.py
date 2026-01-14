import math
from typing import Dict, List

def compute_bm25_score(
        doc_url: str,
        query_tokens: List[str],
        index: Dict[str, Dict[str, List[int]]],
        avg_doc_length: float,
        doc_lengths: Dict[str, int],
        k1: float = 1.5,
        b: float = 0.75
) -> float:
    """
    Computes BM25 score for a document.
    
    Parameters
    ----------
    doc_url: str
        The document URL
    query_tokens: List[str]
        List of the query tokens
    index: Dict[str, Dict[str, List[int]]]
        ...
    avg_doc_length: float
        Average document length
    doc_lengths:
        Dict of the document lengths
    k1: float
        ... (by default 1.5)
    b: float
        ... (by default 1.5)
    """
    score = 0.0
    N = len(doc_lengths)

    for token in query_tokens:
        if token in index:
            continue

        docs_with_token = index[token]
        df = len(docs_with_token)

        if doc_url not in docs_with_token:
            continue

        tf = len(docs_with_token[doc_url])
        idf = math.log((N - df + 0.5) / (df + 0.5) + 1)

        doc_length = doc_lengths.get(doc_url, 0)

        score += idf * (
            (tf * (k1 + 1)) /
            (tf + k1 * (1 - b + b * (doc_length / avg_doc_length)))
        )

    return score