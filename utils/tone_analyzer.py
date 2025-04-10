"""
Tone Analyzer for Resume Decoder

Performs a basic word-frequency-based tone breakdown using categories like corporate,
action-driven, creative, and emotional to simulate tone imbalance detection.
Outputs a simple structure that can be visualized as a chart or summary.
Also supports optional HTML-based inline word highlighting.
"""

from collections import Counter
import re

TONE_CATEGORIES = {
    "corporate": ["synergy", "alignment", "stakeholders", "roadmap", "strategic", "scalable", "initiative"],
    "action": ["led", "built", "created", "developed", "executed", "owned", "initiated"],
    "emotional": ["passionate", "driven", "excited", "eager", "enthusiastic", "empathetic"],
    "creative": ["designed", "crafted", "imagined", "ideated", "visualized", "conceptualized"],
    "fluff": ["dynamic", "self-starter", "go-getter", "team player", "detail-oriented", "hardworking"]
}


def analyze_tone(text: str) -> dict:
    """
    Counts keyword occurrences across tone categories to estimate tone balance.

    Parameters:
        text (str): Raw input text

    Returns:
        dict: Dictionary with tone category names and their counts
    """
    text_lower = text.lower()
    word_list = re.findall(r"\b\w+\b", text_lower)
    tone_counts = Counter()

    for tone, keywords in TONE_CATEGORIES.items():
        for word in word_list:
            if word in keywords:
                tone_counts[tone] += 1

    return dict(tone_counts)


def get_dominant_tone(tone_results: dict) -> str:
    """
    Returns the tone category with the highest count.

    Parameters:
        tone_results (dict): Output of analyze_tone()

    Returns:
        str: Dominant tone category
    """
    if not tone_results:
        return "neutral"
    return max(tone_results, key=tone_results.get)


def highlight_tone_words(text: str) -> str:
    """
    Highlights tone-related keywords in the input text with HTML spans and classes.

    Parameters:
        text (str): Input text to process

    Returns:
        str: HTML string with tone keywords wrapped in <span class="tone-{category}">
    """
    word_list = re.findall(r"\b\w+\b", text)
    highlighted = text

    for tone, keywords in TONE_CATEGORIES.items():
        for kw in sorted(keywords, key=len, reverse=True):
            regex = rf"\b({re.escape(kw)})\b"
            highlighted = re.sub(regex, rf'<span class="tone-{tone}">\1</span>', highlighted, flags=re.IGNORECASE)

    return highlighted
