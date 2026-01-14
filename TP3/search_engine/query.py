from typing import List, Set
from search_engine.tokenizer import tokenize

def parse_query(query: str, stopwords: Set[str]) -> List[str]:
    """
    Parses a raw user query into normalized tokens
    
    Parameters
    ----------
    query: str
        Raw user query
    stopwords: Set[str]
        Stopwords to remove
        
    Return
    ------
    List[str]
        List of normalized query tokens
    """
    if not query:
        return []
    return tokenize(query, stopwords)

