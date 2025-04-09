def render_final_resume(edited_sections, user_profile=None):
    """
    Create a full resume in clean markdown format from edited sections.
    Accepts optional user_profile dict with fields like name, email, phone, linkedin.
    """
    if user_profile is None:
        user_profile = {
            "name": "Your Name",
            "title": "Professional Title or Career Focus",
            "location": "City, State",
            "email": "you@email.com",
            "phone": "(123) 456-7890",
            "linkedin": "linkedin.com/in/yourname",
            "github": "github.com/yourname"
        }

    lines = []

    # Header Section
    lines.append(f"# {user_profile['name']}")
    lines.append(f"**{user_profile['title']}**")
    lines.append(f"{user_profile['location']} · {user_profile['email']} · {user_profile['phone']}")

    if user_profile.get("linkedin") or user_profile.get("github"):
        contact_links = []
        if user_profile.get("linkedin"):
            contact_links.append(f"[LinkedIn]({user_profile['linkedin']})")
        if user_profile.get("github"):
            contact_links.append(f"[GitHub]({user_profile['github']})")
        lines.append(" • ".join(contact_links))

    lines.append("\n---\n")

    # Core Resume Sections
    for section_title, content in edited_sections.items():
        if content.strip():
            lines.append(f"## {section_title}")
            lines.append(content.strip())
            lines.append("\n")

    return "\n".join(lines)
