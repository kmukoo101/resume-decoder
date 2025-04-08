"""
Session Storage Utilities for Resume Decoder

Provides functions for saving and loading session data as JSON. This allows users to export
their decoding results and reload them later into the app.
"""

import json
from typing import Dict

def save_session(filepath: str, session_data: Dict):
    """
    Saves the given session data to a file.

    Parameters:
        filepath (str): Path to the output .json file
        session_data (dict): Data to store (e.g. input, decoded text, style)
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)


def load_session(filepath: str) -> Dict:
    """
    Loads session data from a JSON file.

    Parameters:
        filepath (str): Path to the saved session file

    Returns:
        dict: Restored session data
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_uploaded_session(file_obj) -> Dict:
    """
    Parses a file-like uploaded object (from Streamlit uploader) into session data.

    Parameters:
        file_obj: Uploaded file object

    Returns:
        dict: Parsed session content or empty dict
    """
    try:
        return json.load(file_obj)
    except Exception:
        return {}
