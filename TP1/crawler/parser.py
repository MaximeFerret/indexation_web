from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json

def parse_html(html: str, base_url: str) -> dict:
    """
    Parses the HTML and return useful information
    
    Parameters
    ----------
    html: str
        The HTML raw code we want to parse
    base_url: str
        The URL of this HTML

    Return
    ------
    dict
        The dictionnary containing the title, the first paragraph and the links of the HTML.
    """
    soup = BeautifulSoup(html, "html.parser")

    return {
        "url": base_url,
        "title": extract_title(soup),
        "description": extract_first_paragraph(soup),
        "product_features": extract_product_features(soup), 
        "links": extract_links(soup, base_url),
        "product_reviews": extract_product_reviews(soup)
    }


def extract_title(soup: BeautifulSoup) -> str:
    """
    Extracts the title from an HTML
    
    Parameters
    ----------
    soup: BeautifulSoup
        BeautifulSoup of the given HTML
    
    Return
    ------
    str
        The title
    """
    h1 = soup.select_one("h1")
    if h1 and h1.get_text(strip=True):
        title = h1.get_text(strip=True)
        prefix = "web-scraping.dev product "
        if title.lower().startswith(prefix):
            title = title[len(prefix):]
        return title

    if soup.title and soup.title.string:
        title = soup.title.string.strip()
        prefix = "web-scraping.dev product "
        if title.lower().startswith(prefix):
            title = title[len(prefix):]
        return title

    return ""


def extract_first_paragraph(soup: BeautifulSoup) -> str:
    """
    Extracts the first non-empty paragraph from an HTML
    
    Parameters
    ----------
    soup: BeautifulSoup
        BeautifulSoup of the given HTML
    
    Return
    ------
    str
        The first non-empty paragraph
    """
    for paragraph in soup.find_all("p"):
        text = paragraph.get_text(strip=True)
        if text:
            return text
    return ""


def extract_links(soup: BeautifulSoup, base_url: str) -> list[str]:
    """
    Extracts all links from the page (internal and external), preserving order.

    Parameters
    ----------
    soup: BeautifulSoup
        BeautifulSoup of the given HTML
    base_url: str
        URL of the page, used to resolve relative links

    Returns
    -------
    list[str]
        List of all links found in the HTML
    """
    links = []

    body = soup.body
    if not body:
        return links

    for anchor in body.find_all("a", href=True):
        absolute_url = urljoin(base_url, anchor["href"])
        links.append(absolute_url)

    return links


def extract_product_features(soup: BeautifulSoup) -> dict:
    """
    Extracts product features from the HTML soup.
    
    Parameters
    ----------
    soup: BeautifulSoup
        BeautifulSoup of the given HTML
    
    Return
    ------
    dict
        The product features as a dictionary
    """
    features = {}
    
    for tr in soup.select("tr.feature"):
        label_td = tr.select_one("td.feature-label")
        value_td = tr.select_one("td.feature-value")
        if label_td and value_td:
            label = label_td.get_text(strip=True).lower()  # lowercase comme expected_results
            value = value_td.get_text(strip=True)
            features[label] = value
    return features


def extract_product_reviews(soup: BeautifulSoup) -> list[dict]:
    """
    Extracts product reviews from the HTML soup.

    Parameters
    ----------
    soup: BeautifulSoup
        BeautifulSoup of the given HTML

    Return
    ------
    list[dict]
        The product reviews as a list of dictionaries
    """
    reviews = []
    script_tag = soup.select_one("#reviews-data")
    if script_tag:
        try:
            reviews = json.loads(script_tag.string)
        except json.JSONDecodeError:
            reviews = []
    return reviews