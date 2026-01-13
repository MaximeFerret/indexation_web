from typing import Dict, List

def normalize_feature_value(value: str) -> str:
    """
    Normalize a feature value (lowercase)
    
    Parameters
    ----------
    value: str
        The feature value we want to normalize
    
    Return
    ------
    str
        The normalized feature value
    """
    return value.strip().lower()

def create_feature_index(
        documents: List[dict],
        feature_name: str
) -> Dict[str, List[str]]:
    """
    Creates an inverted index for a given product feature
    
    Parameters
    ----------
    documents: List[dict]
        List of documents
    feature_name: str
        Feature to index (brand, origin, etc.)
    
    Return
    ------
    Dict[str, List[str]]
        Feature inverted index {feature_value: [url, ...]}
    """
    index: Dict[str, List[str]] = {}

    for document in documents:
        url = document.get("url")
        features = document.get("product_features", {})

        if not url or feature_name not in features:
            continue
    
        feature_value = normalize_feature_value(features[feature_name])

        if feature_value not in index:
            index[feature_value] = []

        if url not in index[feature_value]:
            index[feature_value].append(url)
    return index
