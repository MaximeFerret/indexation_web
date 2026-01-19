import difflib

from typing import List, Set

def correct_tokens(
        tokens: List[str],
        vocabulary: Set[str],
        cutoff: float = 0.8
) -> List[str]:
    """
    Corrects query tokens using closet matches in vocabulary.
    
    Parameters
    ----------
    tokens: List[str]
        Tokens we want to correct
    vocabulary: Set[str]
        Set of referenced words
    cutoff: float
        Similarity threshold (by default 0.8)
    
    Return
    ------
    List[str]
        Corrected tokens
    """
    corrected = []

    for token in tokens:
        matches = difflib.get_close_matches(
            token, vocabulary, n=1, cutoff=cutoff
        )
        corrected.append(matches[0] if matches else token)

    return corrected