"""
ATS Compatibility Checker

Performs a basic analysis of resume text to check for common applicant tracking system (ATS) pitfalls,
red flags, and best practices. Returns a dictionary of checks for scoring and display.
"""

import re

REQUIRED_SECTIONS = ["experience", "education", "skills"]
KEYWORDS = ["project management", "python", "data analysis", "communication", "teamwork", "leadership"]
ACTION_VERBS = ["developed", "led", "created", "implemented", "managed", "streamlined"]
BAD_FORMATTING_PATTERNS = ["table", "text box", "header", "footer"]  # simplified for demo


def check_ats_friendly(text: str) -> dict:
    """
    Analyzes text for ATS compatibility using keyword presence, structure, and formatting indicators.

    Parameters:
        text (str): The resume or job description input

    Returns:
        dict: Dictionary with boolean results and score
    """
    text_lower = text.lower()
    results = {}

    # Section checks
    for section in REQUIRED_SECTIONS:
        results[f"has_{section}_section"] = section in text_lower

    # Keyword coverage
    keyword_hits = [kw for kw in KEYWORDS if kw in text_lower]
    results["keyword_coverage"] = len(keyword_hits) / len(KEYWORDS) >= 0.5

    # Action verbs presence
    action_hits = [verb for verb in ACTION_VERBS if re.search(rf"\b{verb}\b", text_lower)]
    results["uses_action_verbs"] = len(action_hits) >= 3

    # Contact info check
    has_email = bool(re.search(r"[\w\.-]+@[\w\.-]+", text))
    has_phone = bool(re.search(r"\+?\d[\d\s\-()]{7,}", text))
    results["has_contact_info"] = has_email and has_phone

    # Bad formatting warning (naive, since we can't see true format in plain text)
    results["possible_formatting_issues"] = any(term in text_lower for term in BAD_FORMATTING_PATTERNS)

    # Final pass score (simple logic)
    pass_criteria = sum(1 for v in results.values() if v is True)
    results["pass_score"] = round((pass_criteria / (len(results) - 1)) * 100)

    return results
