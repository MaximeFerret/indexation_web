import json
import sys
from search_engine.search import search
from search_engine.persistence import save_index


def main():
    """
    Entry point for the search engine.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your search query\"")
        sys.exit(1)

    query = sys.argv[1]
    results = search(query)

    print(json.dumps(results, ensure_ascii=False, indent=2))

    save_index(results, "output/results.json")

if __name__ == "__main__":
    main()
