from search_engine.tokenizer import normalize_text


def compute_exact_match_score(
        title: str,
        description: str,
        query: str
) -> float:
    """
    Computes an exact match score using normalized full-word matching
    
    Parameters
    ----------
    title: str
        Title of the document or entity
    description: str
        Document description
    query: str
        User query submitted
    
    Return
    ------
    float
        The exact match score : 2 if query in title, 1 if query in description, 0 else
    """
    normalized_query = normalize_text(query).strip()
    normalized_title = normalize_text(title)
    normalized_description = normalize_text(description)

    # pad the query, title and description will allow to avoid false positive matchs
    padded_query = f" {normalized_query} "
    padded_title = f" {normalized_title} "
    padded_description = f" {normalized_description} "

    if padded_query in padded_title:
        return 2.0
    
    if padded_query in padded_description:
        return 1.0
    
    return 0.0