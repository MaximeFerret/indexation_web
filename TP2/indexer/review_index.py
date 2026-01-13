from typing import Dict, List

def compute_review_statistics(reviews: List[dict]) -> Dict[str, float | int]:
    """
    Computes statistics from product reviews
    
    Parameters
    ----------
    reviews: List[dict]
        List of review objects
        
    Return
    ------
    Dict[str, float | int]
        Review statistics
    """
    if not reviews:
        return {
            "total_reviews": 0,
            "mean_mark": 0,
            "last_rating": 0
        }
    
    total_reviews = len(reviews)
    ratings = [review.get("rating", 0) for review in reviews]

    mean_mark = sum(ratings)/total_reviews

    last_rating = ratings[-1]

    return {
        "total_reviews": total_reviews,
        "mean_mark": round(mean_mark, 2),
        "last_rating": last_rating
    }


def create_review_index(documents: List[dict]) -> Dict[str, Dict]:
    """
    Creates a review index for all documents
    
    Parameters
    ----------
    documents: List[dict]
        List of documents we want to create a review index
        
    Return
    ------
    Dict[str, Dict]
        Review index {url: review_stats}
    """
    index: Dict[str, Dict] = {}

    for document in documents:
        url = document.get("url")
        reviews = document.get("product_reviews", [])

        if not url:
            continue

        index[url] = compute_review_statistics(reviews)

    return index