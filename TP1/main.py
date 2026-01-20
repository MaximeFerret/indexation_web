from crawler.crawler import crawl
from crawler.storage import save_jsonl

if __name__ == "__main__":
    start_url = "https://web-scraping.dev/products"

    results = crawl(start_url, max_pages=10, delay=1.0)
    save_jsonl(results, "data/results.jsonl")

    # Tests with different start URLs
    crawl("https://web-scraping.dev/products", max_pages=10)
    crawl("https://web-scraping.dev/", max_pages=10)