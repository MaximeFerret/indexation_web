import json
from typing import Dict

def save_index(index: Dict, file_path: str) -> None:
    """
    Saves an index to a JSON file
    
    Parameters
    ----------
    index: Dict
        Index to save
    file_path: str
        Path to output JSON file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(index, file, ensure_ascii=False, indent=2)

def load_index(file_path: str) -> Dict:
    """
    Loads an index from a JSON file
    
    Parameters
    ----------
    file_path: str
        Path to JSON file
        
    Return
    ------
    Dict
        Loaded index
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)