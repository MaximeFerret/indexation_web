import json
from typing import List, Dict

def load_jsonl(path: str) -> list[dict]:
    """Loads a JSONL file into a list of dicts.
    
    Parameters
    ----------
    path: str
        Path to the JSONL file.
    
    Return
    ------
    list[dict]
        List of dicts loaded from the file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def save_jsonl(results: List[Dict], filename: str) -> None:
    """
    Saves results into JSONL file.

    Parameters
    ----------
    results: List[Dict]
        Results we want to save.
    filename: str
    """
    with open(filename, "w", encoding="utf-8") as f:
        for page in results:
            json.dump(page, f, ensure_ascii=False)
            f.write("\n")