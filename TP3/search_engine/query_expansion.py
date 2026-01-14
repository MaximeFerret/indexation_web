from typing import List, Dict

def expand_query_with_synonyms(
        tokens: List[str],
        synonyms: Dict[str, List[str]]
) -> List[str]:
    """
    Expands query tokens using a synonym dictionary
    
    Parameters
    ----------
    tokens: List[str]
        Initial query tokens
    synonyms: Dict[str, List[str]]
        Synonym dictionary
    
    Return
    ------
    List[str]
        Expanded list of query tokens
    """
    expanded_tokens = set(tokens)

    for token in tokens:
        if token in synonyms:
            for synonym in synonyms[token]:
                expanded_tokens.add(synonym)

    return list(expanded_tokens)