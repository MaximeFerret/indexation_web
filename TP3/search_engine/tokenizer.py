import string
from typing import List, Set

def normalize_text(text: str) -> str:
    """
    Normalizes text by lowering case and removing punctuation.
    
    Parameters
    ----------
    text: str
        The text we want to normalize.
        
    Return
    ------
    str
        The normalized text
    """
    text = text.lower()

    for puntuation in string.punctuation:
        text = text.replace(puntuation, "")
    
    return text


def tokenize(text: str, stopwords: Set[str]) -> List[str]:
    """
    Tokenizes text by spaces and remove stopwords
    
    Parameters
    ----------
    text: str
        The text we want to tokenize
    stopwords: Set[str]
        The set of useless words we want to remove
    """
    normalized_text = normalize_text(text)
    tokens = normalized_text.split()
    return [token for token in tokens if token not in stopwords]
