from typing import List, Dict, Set

def filter_documents_any_token(
        tokens: List[str],
        indexes: Dict[str, Dict[str, List[str]]]
) -> Set[str]:
    """
    Filters documents that contain at least one query token
    
    Parameters
    ----------
    tokens: List[str]
        Query tokens
    indexes: Dict[str, Dict[str, List[str]]]
        Inverted indexes (title, description, brand, origin, ...)

    Return
    ------
    Set[str]
        Set of document URLs
    """
    matched_documents: Set[str] = set()
    for token in tokens:
        for index in indexes.values():
            if token in index:
                matched_documents.update(index[token])

    return matched_documents


def filter_documents_all_tokens(
        tokens: List[str],
        indexes: Dict[str, Dict[str, List[str]]],
        stopwords: Set[str]
) -> Set[str]:
    """
    Filters documents that contain all query tokens except stopwords.
    
    Parameters
    ----------
    tokens: List[str]
        Query tokens
    indexes: Dict[str, Dict]
        Inverted indexes
    stopwords: Set[str]
        Stopwords to ignore
        
    Return
    ------
    Set[str]
        Set of document URLs
    """
    filtered_tokens = [t for t in tokens if t not in stopwords]

    if not filtered_tokens:
        return set()
    
    document_sets = []

    for token in filtered_tokens:
        token_documents = set()
        for index in indexes.values():
            if token in index:
                token_documents.update(index[token])
        document_sets.append(token_documents)

    return set.intersection(*document_sets) if document_sets else set()