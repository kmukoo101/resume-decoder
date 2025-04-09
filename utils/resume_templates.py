def render_resume_preview(name, title_focus, location, email, phone, linkedin, github, sections):
    """
    Returns formatted markdown for a clean, modern resume.
    """
    contact_info = f"{location} · [{email}](mailto:{email}) · {phone}"
    if linkedin:
        contact_info += f" · [LinkedIn]({linkedin})"
    if github:
        contact_info += f" · [GitHub]({github})"

    markdown = f"# {name}\n**{title_focus}**  \n{contact_info}\n\n---\n"

    for section_title, content in sections.items():
        markdown += f"### {section_title}\n{content.strip()}\n\n"

    return markdown

