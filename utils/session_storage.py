"""
Session Storage Utilities for Resume Decoder

Provides functions for saving and loading session data as JSON. This allows users to export
their decoding results and reload them later into the app. Also supports saving tone, ATS,
and quality score results to preserve full state.
"""

import json
from typing import Dict, Optional

def save_session(filepath: str, session_data: Dict):
    """
    Saves the given session data to a file.

    Parameters:
        filepath (str): Path to the output .json file
        session_data (dict): Data to store (e.g. input, decoded text, style, scores)
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

def create_export_bundle(
    input_text: str,
    decoded: str,
    style: str,
    buzzword_score: float,
    tone_results: Dict,
    ats_results: Dict,
    quality_score: Optional[int] = None
) -> Dict:
    """
    Builds a structured session dictionary for exporting full results.

    Parameters:
        input_text (str): Original user input
        decoded (str): Decoded output
        style (str): Style used
        buzzword_score (float): Score of buzzwords
        tone_results (dict): Output from tone analyzer
        ats_results (dict): ATS compliance flags
        quality_score (int, optional): Calculated overall resume quality score

    Returns:
        dict: JSON-ready export object
    """
    return {
        "input": input_text,
        "decoded": decoded,
        "style": style,
        "buzzword_score": buzzword_score,
        "tone": tone_results,
        "ats": ats_results,
        "quality_score": quality_score
    }
