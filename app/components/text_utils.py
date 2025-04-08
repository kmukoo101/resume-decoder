"""
Text Utilities for Resume Decoder

This module provides the core logic for:
- Detecting buzzwords in text
- Rewriting text in different tones/styles
- Scoring the density of corporate jargon
- Highlighting detected buzzwords in original text

Used by both the main decoder page and examples page.
"""

import re
from typing import Tuple, Dict

def decode_text(input_text: str, buzzword_dict: Dict[str, str], style: str = "Plain English") -> Tuple[str, int, str]:
    """
    Decodes the input resume or job description text by identifying and translating buzzwords
    into more honest or humorous equivalents.

    Parameters:
        input_text (str): The text to decode.
        buzzword_dict (dict): Mapping of buzzwords to plain/honest interpretations.
        style (str): Chosen decoding style. Options include:
                     "Plain English", "Real Talk", "Gen Z", "Corporate Satire"

    Returns:
        Tuple[str, int, str]:
            - decoded_text: The rewritten version of the text
            - score: % of buzzwords detected in the original
            - highlighted_text: HTML-formatted version of original text with buzzwords highlighted
    """
    # Normalize and tokenize
    original_words = re.findall(r'\b\w[\w\-]*\b', input_text.lower())

    detected_buzzwords = [word for word in original_words if word in buzzword_dict]
    total_words = len(original_words)
    score = round(len(detected_buzzwords) / total_words * 100, 2) if total_words > 0 else 0

    # Highlight original text
    highlighted_text = highlight_buzzwords(input_text, buzzword_dict)

    # Rewrite text in selected style
    decoded_text = rewrite_text(input_text, buzzword_dict, style)

    return decoded_text, score, highlighted_text


def highlight_buzzwords(text: str, buzzword_dict: Dict[str, str]) -> str:
    """
    Highlights buzzwords in the original text using HTML <mark> tags.

    Parameters:
        text (str): Original input text
        buzzword_dict (dict): Buzzword lookup dictionary

    Returns:
        str: HTML string with buzzwords highlighted
    """
    def highlight(match):
        word = match.group(0)
        lower_word = word.lower()
        if lower_word in buzzword_dict:
            return f"<mark title='{buzzword_dict[lower_word]}'>{word}</mark>"
        return word

    # Use regex to match words only (preserves punctuation)
    highlighted = re.sub(r'\b\w[\w\-]*\b', highlight, text)
    return highlighted


def rewrite_text(text: str, buzzword_dict: Dict[str, str], style: str) -> str:
    """
    Rewrites the input text by replacing buzzwords with alternate phrasings
    depending on the selected decoding style.

    Parameters:
        text (str): Original input text
        buzzword_dict (dict): Dictionary of buzzword → plain translation
        style (str): Style to rewrite in ("Plain English", "Real Talk", etc.)

    Returns:
        str: Rewritten, decoded text
    """
    def translate(word: str) -> str:
        lower = word.lower()
        if lower in buzzword_dict:
            base = buzzword_dict[lower]
            # Customize translation style
            if style == "Plain English":
                return base
            elif style == "Real Talk":
                return f"[💬 Translation: {base}]"
            elif style == "Gen Z":
                return f"{word} (lol basically: {base})"
            elif style == "Corporate Satire":
                return f"{word}™️ ({base})"
        return word

    # Reconstruct sentence with style-based replacements
    words = re.findall(r'\b\w[\w\-]*\b|\W+', text)
    rewritten = "".join([translate(w) if re.match(r'\w[\w\-]*', w) else w for w in words])
    return rewritten

