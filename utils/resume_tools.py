import re
from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text, top_n=15):
    """Extract top N keywords using simple frequency analysis."""
    vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()

def match_keywords(job_keywords, resume_keywords):
    """Compare job and resume keyword sets and return match info."""
    job_set = set(job_keywords)
    resume_set = set(resume_keywords)

    matched = job_set & resume_set
    missing = job_set - resume_set
    match_percent = round(len(matched) / len(job_set) * 100) if job_set else 0

    return {
        "matched_keywords": list(matched),
        "missing_keywords": list(missing),
        "match_percent": match_percent
    }

def suggest_resume_sections(job_description):
    """Suggest resume sections based on content of job description."""
    lower_text = job_description.lower()
    suggestions = []

    if 'communication' in lower_text:
        suggestions.append('Communication Skills')
    if 'leadership' in lower_text:
        suggestions.append('Leadership Experience')
    if 'project' in lower_text or 'manage' in lower_text:
        suggestions.append('Project Management')
    if 'sql' in lower_text or 'python' in lower_text:
        suggestions.append('Technical Skills')
    if 'customer' in lower_text:
        suggestions.append('Customer Service')
    if 'data' in lower_text:
        suggestions.append('Data Analysis')

    return list(set(suggestions))
