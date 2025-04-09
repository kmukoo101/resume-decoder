import re
from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text, top_n=15):
    """Extract top N keywords using simple frequency analysis."""
    vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()

def match_keywords(job_keywords, resume_text):
    """Check which job keywords appear in the resume."""
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    matched = [kw for kw in job_keywords if kw.lower() in resume_words]
    missing = [kw for kw in job_keywords if kw.lower() not in resume_words]
    return matched, missing

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
