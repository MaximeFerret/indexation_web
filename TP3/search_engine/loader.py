import json
from typing import List, Dict

def load_jsonl(file_path: str) -> List[Dict]:
    """
    Load a JSONL file and return a list of dictionaries.
    
    Parameters
    ----------
    file_path: str
        The file path JSONL we want to load.
    
    Return
    ------
    List[Dict]
        A document list of the given JSONL
    """
    documents = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, lin in enumerate(file, start=1):
            line=line.strip()
            if not line:
                continue

            try:
                document = json.loads(line)
                documents.append(document)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON at line {line_number}: {e}")
    
    return documents


def load_json(file_path: str) -> Dict:
    """
    Load a JSON file and return its content
    
    Parameters
    ----------
    file_path: str
        The file path JSONL we want to load.
    
    Return
    ------
    Dict
        A dict of the given JSON
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
