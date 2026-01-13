from typing import Dict, List, Set
from indexer.tokenizer import tokenize, normalize_text

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

def create_position_index(
        documents: List[dict],
        field: str,
        stopwords: Set[str]
) -> Dict[str, Dict[str, List[int]]]:
    """
    Creates an inverted index with token positions for a given txt field
    
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
    Dict[str, Dict[str, List[int]]]
        Position index {token: {url: [positions]}}
    """
    index: Dict[str, Dict[str, List[int]]] = {}

    for document in documents:
        url = document.get("url")
        text = document.get(field, "")

        if not url or not text:
            continue
        
        normalized_text = normalize_text(text)
        tokens = normalized_text.split()

        position = 0
        for token in tokens:
            if token in stopwords:
                position += 1
                continue

            if token not in index:
                index[token] = {}

            if url not in index[token]:
                index[token][url] = []
            
            index[token][url].append(position)
            position += 1

    return index

