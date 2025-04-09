from sklearn.feature_extraction.text import CountVectorizer

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

def suggest_resume_sections(job_description, resume_text):
    lower_text = job_description.lower()
    resume_lower = resume_text.lower()
    sections = []

    if 'communication' in lower_text:
        sections.append({'title': 'Communication Skills', 'content': 'Demonstrated ability to clearly convey ideas and collaborate with cross-functional teams.'})

    if 'leadership' in lower_text:
        sections.append({'title': 'Leadership Experience', 'content': 'Led teams and initiatives with a focus on mentorship, delegation, and strategic outcomes.'})

    if 'project' in lower_text or 'manage' in lower_text:
        sections.append({'title': 'Project Management', 'content': 'Experienced in managing timelines, budgets, and deliverables for technical and operational projects.'})

    if 'sql' in lower_text or 'python' in lower_text:
        sections.append({'title': 'Technical Skills', 'content': 'Proficient in Python and SQL for data analysis, automation, and reporting.'})

    if 'customer' in lower_text:
        sections.append({'title': 'Customer Service', 'content': 'Skilled in delivering customer satisfaction through empathy, responsiveness, and efficiency.'})

    if 'data' in lower_text:
        sections.append({'title': 'Data Analysis', 'content': 'Analyzed trends and patterns to derive insights using statistical tools and data visualization techniques.'})

    # Add fallback if no section suggestions found
    if not sections:
        sections.append({'title': 'Summary', 'content': resume_text[:500]})

    return sections
