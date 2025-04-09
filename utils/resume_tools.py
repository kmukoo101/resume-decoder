import re
from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text):
    # Tokenize and vectorize the text
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return list(keywords)

def match_keywords(job_keywords, resume_keywords):
    job_set = set(job_keywords)
    resume_set = set(resume_keywords)
    matched = job_set.intersection(resume_set)
    missing = job_set.difference(resume_set)
    match_percent = (len(matched) / len(job_set)) * 100 if job_set else 0

    return {
        "match_percent": round(match_percent, 2),
        "matched_keywords": list(matched),
        "missing_keywords": list(missing)
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
