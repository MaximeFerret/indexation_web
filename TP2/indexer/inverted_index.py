from typing import Dict, List, Set
from indexer.tokenizer import tokenize

def create_inverted_index(
        documents: List[dict],
        field: str,
        stopwords: Set[str]
) -> Dict[str, List[str]]:
    """
    Creates an inverted index for a given text field
    
    Parameters
    ----------
    documents: List[dict]
        List of documents
    field: str
        Field to index (title or description)
    stopwords: Set[str]
        Stopwords to remove
    
    Return
    ------
    Dict[str, List[str]]
        Dict of inverted index of the given text field {token: [url, ....]}
    """
    index: Dict[str, List[str]] = {}

    for document in documents:
        url = document.get("url")
        text = document.get(field, "")

        if not url or not text:
            continue

        tokens = tokenize(text, stopwords)

        for token in tokens:
            if token not in index:
                index[token] = []

            if url not in index[token]:
                index[token].append(url)
    return index