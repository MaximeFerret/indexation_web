from urllib.parse import urlparse, parse_qs
import re

def extract_product_id(url: str) -> str | None:
    """
    Extracts product ID from a product URL
    
    Parameters
    ----------
    url: str
        The product URL
        
    Return
    ------
    str
        The product ID
    """
    parsed_url = urlparse(url)
    path = parsed_url.path

    match = re.search(r"/product/(\d+)", path)
    if match:
        return match.group(1)
    
    return None

def extract_variant(url: str) -> str | None:
    """
    Extracts variant parameter from URL if present.
    
    Parameters
    ----------
    url: str
        The product URL
    
    Return
    ------
    str
        Variant parameter
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    variant = query_params.get("variant")
    if variant:
        return variant[0]
    return None

