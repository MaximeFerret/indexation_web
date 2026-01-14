from typing import Dict

def compute_linear_score(
    features: Dict[str, float],
    weights: Dict[str, float]
) -> float:
    """
    Computes a linear combination of features
    
    Parameters
    ----------
    features: Dict[str, float]
        Dictionary mapping feature names to their numerical values
    wieghts: Dict[str, float]
        Dictionary mapping feature names to their corresponding weights ex: {"bm25_title": 2.0, "bm25_description": 1.0, "exact_match": 2.0, ...}

    Return
    ------
    float
        The computed linear score
    """
    score = 0.0

    for feature, value in features.items():
        score += weights.get(feature, 0.0) * value
    return score