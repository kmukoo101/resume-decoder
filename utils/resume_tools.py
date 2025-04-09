from sklearn.feature_extraction.text import CountVectorizer
import fitz  # PyMuPDF

def extract_keywords(text):
    if not text or not isinstance(text, str):
        return []

    vectorizer = CountVectorizer(stop_words='english')
    try:
        X = vectorizer.fit_transform([text])
        keywords = vectorizer.get_feature_names_out()
        return list(keywords)
    except Exception as e:
        print(f"[Keyword Extraction Error]: {e}")
        return []

def load_text_from_file(file):
    try:
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            text = "\n".join([page.get_text() for page in doc])
        return text.strip()
    except Exception as e:
        print(f"[File Loader Error]: {e}")
        return ""

def match_keywords(job_keywords, resume_keywords):
    if not isinstance(job_keywords, list) or not isinstance(resume_keywords, list):
        job_keywords = job_keywords or []
        resume_keywords = resume_keywords or []

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
