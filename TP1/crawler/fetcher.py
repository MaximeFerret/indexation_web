import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

def initialise_robots_parser(url: str) -> RobotFileParser:
    """
    Initialises and returns a RobotFileParser for a given domain.
    This function will load the robots.txt of this domain.

    Parameters
    ----------
    url: str
        The url of a given domain

    Return
    ------
    RobotFileParser
        The robot parser of a given domain
    """
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

    robot_parser = RobotFileParser()
    robot_parser.set_url(robots_url)

    try:
        robot_parser.read()
    except Exception:
        print(f"robots.txt inaccessible for: {url} \n Access assumed to be authorised by default.")

    return robot_parser


def can_fetch_url(robot_parser: RobotFileParser, url: str, user_agent: str = "*") -> bool:
    """
    Checks if the crawler is allowed to access to an URL
    
    Parameters
    ----------
    robot_parser: RobotFileParser
        The robot parser of the domain's URL
    url: str
        The URL we want to check the access authorisation
    user_agent: str
        The agent name of our crawler (by default "*")

    Return
    ------
    bool
        True if we are allowed to access, False else
    """
    return robot_parser.can_fetch(user_agent, url)


def fetch_html(url: str, timeout: int = 10) -> str | None:
    """
    Retrieves the HTML of an URL
    
    Parameters
    ----------
    url: str
        The URL we want to fetch
    timeout: int
        In seconds, the timeout for blocking operations like the connection attempt (by default 10sec) 
    
    Return
    ------
    str
        The HTML of the given URL
    """
    headers = {
        "User-Agent": "SimpleWebCrawler/1.0"
    }

    request = Request(url, headers=headers)

    try:
        with urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get("Content-Type", "")
            if "text/html" not in content_type:
                return None
            
            html = response.read().decode("utf-8", errors="ignore")
            return html
        
    except HTTPError as e:
        print(f"HTTP error {e.code} for URL: {url}")
    except URLError as e:
        print(f"URL error for URL: {url} -> {e.reason}")
    except Exception as e:
        print(f"Unexpected error for URL: {url} -> {e}")

    return None


def apply_politeness(delay: float = 1.0) -> None:
    """
    Applies a delay between two HTTP requests

    Parameters
    ----------
    delay: float
        In second, the delay we want to apply
    
    Return
    ------
    None
    """
    time.sleep(delay)


