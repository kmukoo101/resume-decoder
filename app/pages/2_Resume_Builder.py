"""
Resume Builder Page

This Streamlit page helps users build an ATS-optimized resume by combining:
- a job description,
- an existing resume,
- and keyword analysis.

Features:
- Upload or paste job description
- Upload or paste current resume
- Keyword gap analysis (between job & resume)
- Matching score / fit %
- AI-suggested improvements per section
- Editable text blocks for each section
- Export as ATS-ready PDF or DOCX
"""
from utils.resume_template import render_resume_preview
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.resume_tools import extract_keywords, match_keywords, suggest_resume_sections
from utils.file_loader import load_text_from_file
from utils.resume_templates import render_final_resume
from utils.export import export_to_docx
import json

st.title("Resume Builder")
st.caption("Rebuild your resume based on a job description and your current resume.")

# ------------------------
# Inputs: Job & Resume
# ------------------------
col1, col2 = st.columns(2)

with col1:
    job_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"], key="job")
    job_text = st.text_area("Or paste job description", height=300)
    if job_file:
        job_text = load_text_from_file(job_file)

with col2:
    resume_file = st.file_uploader("Upload Current Resume", type=["pdf", "docx", "txt"], key="resume")
    resume_text = st.text_area("Or paste current resume", height=300)
    if resume_file:
        resume_text = load_text_from_file(resume_file)

if job_text and resume_text:
    st.markdown("---")
    st.subheader("Job Match Analysis")

    job_keywords = extract_keywords(job_text)
    resume_keywords = extract_keywords(resume_text)
    match_result = match_keywords(job_keywords, resume_keywords)

    st.write(f"**Match Score:** {match_result['match_percent']}%")
    st.progress(int(match_result['match_percent']))

    if match_result['missing_keywords']:
        st.warning("Missing Keywords:")
        st.markdown(", ".join(match_result['missing_keywords']))

    st.markdown("---")
    st.subheader("Resume Suggestions")

    sections = suggest_resume_sections(job_text, resume_text)
    edited_sections = {}

    for section in sections:
        with st.expander(section['title'], expanded=True):
            edited_text = st.text_area("Edit this section", value=section['content'], height=200)
            edited_sections[section['title']] = edited_text

    if st.button("Export as DOCX"):
        docx_data = export_to_docx(edited_sections)
        st.download_button(
            label="Download ATS Resume",
            data=docx_data,
            file_name="ATS_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

else:
    st.info("Please provide both a job description and your current resume.")


# Render preview markdown
resume_md = render_resume_preview(
    name=full_name,
    title_focus=title_focus,
    location=city_state,
    email=email,
    phone=phone,
    linkedin=linkedin,
    github=github,
    sections=edited_sections
)

st.markdown("## Final Resume Preview")
st.markdown(resume_md, unsafe_allow_html=True)

st.download_button("Download Markdown Version", data=resume_md, file_name="final_resume.md")
st.text_area("Copy-Friendly Markdown", resume_md, height=300)



st.markdown(f"# {full_name}")
st.markdown(f"**{title_focus}**  \n{city_state} · [{email}](mailto:{email}) · {phone} · [LinkedIn]({linkedin}) · [GitHub]({github})")

st.markdown("---")

for section_title, content in edited_sections.items():
    st.markdown(f"### {section_title}")
    st.markdown(content)


markdown_export = f"# {full_name}\n**{title_focus}**  \n{city_state} · {email} · {phone} · {linkedin} · {github}\n\n"
for section_title, content in edited_sections.items():
    markdown_export += f"## {section_title}\n{content}\n\n"

st.download_button(
    "Download Markdown Version",
    data=markdown_export,
    file_name="final_resume.md",
    mime="text/markdown"
)

st.text_area("Copy-Friendly Markdown", markdown_export, height=300)

