from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

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
        "product_features": {}, 
        "links": extract_internal_links(soup, base_url),
        "product_reviews": []
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
    if soup.title and soup.title.string:
        return soup.title.string.strip()
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


def extract_internal_links(soup: BeautifulSoup, base_url: str) -> list[dict]:
    """
    Extracts internal links and indicates source page
    
    Parameters
    ----------
    soup: BeautifulSoup
        BeautifulSoup of the given HTML
    base_url: 
        base_url: str
        The URL of this HTML

    Return
    ------
    list[dict]
        List of dictionnaries like: [{"url": "https://example.com", "from": "https://example.com/2"}]
    """
    links = []
    seen = set()

    base_domain = urlparse(base_url).netloc
    body = soup.body

    if not body:
        return links

    for anchor in body.find_all("a", href=True):
        href = anchor["href"]
        absolute_url = urljoin(base_url, href)
        parsed_url = urlparse(absolute_url)

        if parsed_url.netloc != base_domain:
            continue

        if absolute_url in seen:
            continue

        seen.add(absolute_url)

        links.append({
            "url": absolute_url,
            "from": base_url
        })

    return links