import json
import os
from search_engine.search import search

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def run_tests():
    test_file = os.path.join(BASE_DIR, "tests", "test_queries.json")
    output_file = os.path.join(BASE_DIR, "output", "test_results.json")

    with open(test_file, "r", encoding="utf-8") as file:
        test_queries = json.load(file)

    results = []

    for test in test_queries:
        query = test["query"]
        output = search(query)

        results.append({
            "query": query,
            "description": test["description"],
            "filtered_documents": output["filtered_documents"],
            "top_results": output["results"][:3]
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Tests completed. Results saved to output/test_results.json")


if __name__ == "__main__":
    run_tests()
