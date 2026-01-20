from collections import defaultdict
from crawler.storage import load_jsonl

EXPECTED_PATH = "data/expected_results.jsonl"
RESULTS_PATH = "data/results.jsonl"

def sort_by_url(pages: list[dict]) -> list[dict]:
    """
    Sorts pages by URL.
    
    Parameters
    ----------
    pages: list[dict]
        List of page dicts to sort
    
    Return
    ------
    list[dict]
        Sorted list of page dicts
    """
    return sorted(pages, key=lambda x: x.get("url", ""))


def compare_pages(expected: dict, result: dict) -> list[str]:
    """
    Compares two pages and return list of keys that differ
    
    Parameters
    ----------
    expected: dict
        Expected page data
    result: dict
        Result page data
        
    Return
    ------
    list[str]
        List of keys that differ between expected and result
    """
    diffs = []

    keys_to_compare = [
        "title",
        "description",
        "links",
        "product_features",
        "product_reviews"
    ]

    for key in keys_to_compare:
        if expected.get(key) != result.get(key):
            diffs.append(key)

    return diffs


def main():
    expected_pages = sort_by_url(load_jsonl(EXPECTED_PATH))
    result_pages = sort_by_url(load_jsonl(RESULTS_PATH))

    expected_dict = defaultdict(list)
    for page in expected_pages:
        expected_dict[page["url"]].append(page)

    result_dict = defaultdict(list)
    for page in result_pages:
        result_dict[page["url"]].append(page)

    expected_urls = set(expected_dict.keys())
    result_urls = set(result_dict.keys())

    print("=== URL CHECK ===")
    missing_urls = expected_urls - result_urls
    extra_urls = result_urls - expected_urls

    if not missing_urls and not extra_urls:
        print("URLs match perfectly")
    else:
        if missing_urls:
            print(f"Missing URLs ({len(missing_urls)})")
            # Uncomment to see missing URLs
            # for url in missing_urls:
            #     print("  -", url)
        if extra_urls:
            print(f"Extra URLs ({len(extra_urls)}):")
            # Uncomment to see extra URLs
            # for url in extra_urls:
            #     print("  -", url)

    print("\n=== CONTENT CHECK ===")
    differences_found = False
    for url in expected_urls & result_urls:
        expected_list = expected_dict[url]
        result_list = result_dict[url]

        for _, (exp_page, res_page) in enumerate(zip(expected_list, result_list), 1):
            diffs = compare_pages(exp_page, res_page)
            if diffs:
                differences_found = True
                print(f"[Warning] Differences for {url}: {diffs}")
    if not differences_found:
        print("All pages content match expected results")


if __name__ == "__main__":
    main()
