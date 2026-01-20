from collections import deque
from crawler.fetcher import fetch_html, initialise_robots_parser, can_fetch_url, apply_politeness
from crawler.parser import parse_html

def crawl(start_url: str, max_pages: int = 50, delay: float = 1.0) -> list[dict]:
    """
    Crawls pages from a starting URL with priority given to “product” pages

    Parameters
    ----------
    start_url: str
        The starting URL
    max_pages: int
        Maximum number of pages to crawl
    delay: float
        Delay between requests to respect politeness

    Return
    ------
    list[dict]
        List of crawled page data
    """
    queue = deque([start_url])
    visited = set()
    results = []
    robot_parser = initialise_robots_parser(start_url)

    while queue and len(visited) < max_pages:
        current_url = queue.popleft()

        if current_url in visited:
            continue

        if not can_fetch_url(robot_parser, current_url):
            print(f"Access denied by robots.txt : {current_url}")
            continue

        html = fetch_html(current_url)
        apply_politeness(delay)

        if html is None:
            continue

        page_data = parse_html(html, current_url)
        results.append(page_data)
        visited.add(current_url)

        for link in page_data["links"]:
            if link not in visited and link not in queue:
                if "product" in link:
                    queue.appendleft(link)
                else:
                    queue.append(link)

        print(f"Crawled ({len(visited)}/{max_pages}): {current_url}")

    return results
