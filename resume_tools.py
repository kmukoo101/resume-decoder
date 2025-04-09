import re
from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text, top_n=20):
    """Extract most frequent keywords (basic NLP)."""
    vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return list(keywords)

def match_keywords(resume_text, job_text):
    """Find matching keywords between resume and job description."""
    resume_kw = set(extract_keywords(resume_text))
    job_kw = set(extract_keywords(job_text))
    matches = resume_kw.intersection(job_kw)
    missing = job_kw - resume_kw
    return {
        "matched": list(matches),
        "missing": list(missing),
        "match_percent": round(100 * len(matches) / max(len(job_kw), 1), 1)
    }

def suggest_rewrites(resume_text, missing_keywords):
    """Suggest resume edits to include missing keywords."""
    suggestions = []
    for word in missing_keywords:
        suggestions.append(f"Consider adding a bullet or sentence about '{word}' to match the job post.")
    return suggestions
