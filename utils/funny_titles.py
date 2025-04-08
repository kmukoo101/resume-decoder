"""
Funny Title Generator for Resume Decoder

Provides dynamic, randomly generated mock job titles to reflect
how resumes *actually* sound when decoded.
"""

import random

# Categories of titles
TITLE_CATEGORIES = {
    "general": [
        "Chaos Coordinator",
        "Underpaid Overachiever",
        "VP of Vibes",
        "Director of Making It Look Like It Works",
        "Email Apology Specialist",
        "Meeting Escape Artist",
        "Office Plant Watering Consultant",
        "Corporate Shrug Machine",
        "Slide Deck Sorcerer",
        "Team Morale Micro-Manager"
    ],
    "tech": [
        "Buzzword Alchemist",
        "Full-Stack Blame Magnet",
        "Legacy System Whisperer",
        "Agile-ish Evangelist",
        "404 Solution Not Found Engineer",
        "DevOps Firefighter",
        "Backlog Evangelist",
        "Container Whisperer",
        "Junior Senior Architect",
        "Infinite Sprint Participant"
    ],
    "corporate": [
        "PowerPoint Necromancer",
        "Crisis Response Specialist",
        "Professional Time Blocker",
        "Middle Management Martyr",
        "Quarterly Goal Mumbler",
        "Synergy Czar",
        "KPI Dream Weaver",
        "Watercooler Strategist",
        "Budget Overpromise Coordinator",
        "Reorg Enthusiast"
    ],
    "creative": [
        "Brand Wizard",
        "Pixel Pusher-in-Chief",
        "Aesthetic Optimization Engineer",
        "Vibe Strategist",
        "Moodboard Magician",
        "Chief Canva Officer",
        "Logo Iteration Lead",
        "Color Theory Theorist",
        "Style Guide Enforcer",
        "Typography Whisperer"
    ],
    "burnout": [
        "Late-Stage Capitalism Survivor",
        "Mental Gymnastics Champion",
        "Email Ninja with Carpal Tunnel",
        "Coffee-Driven Doer of All Things",
        "Zoom Fatigue Analyst",
        "Dead Inside but Still Responsive",
        "Burnout Brand Ambassador",
        "Self-Care Reminder Ignorer",
        "Remote Work Existentialist",
        "Lunch-Skipping Productivity Hero"
    ]
}

# Optional seriousness levels (0 = chaotic satire, 3 = realistic parody)
TIERED_TITLES = {
    0: [
        "Professional Apologizer",
        "Wizard of Winging It",
        "Just Happy to Be Included",
        "Excel Cell Sorcerer",
        "Dream Crusher Intern",
        "Google Docs Gladiator",
        "Panic Mode Project Manager",
        "Last Minute Hero",
        "Slack Emoji Interpreter",
        "Desk Plant Psychologist"
    ],
    1: [
        "Senior Alignment Specialist",
        "Cross-Functional Liaison",
        "Employee of the Month (Pending)",
        "Strategic Delay Coordinator",
        "Workflow Navigator",
        "Email Chain Archaeologist",
        "Morale Management Analyst",
        "Interdepartmental Peacekeeper",
        "Data Formatting Champion",
        "Influence Without Authority Specialist"
    ],
    2: [
        "People-First Process Designer",
        "Efficiency Enhancement Lead",
        "Head of Making It Work Somehow",
        "Results Optimization Analyst",
        "Operational Insights Coordinator",
        "Collaboration Strategy Advisor",
        "Resource Forecast Engineer",
        "Performance Mapping Facilitator",
        "Execution Experience Consultant",
        "Goals-to-Reality Translator"
    ],
    3: [
        "Resume Realist",
        "Narrative Reframing Officer",
        "Language Optimization Analyst",
        "Experience Framing Specialist",
        "Professional Impact Designer",
        "Role Description Architect",
        "Talent Positioning Consultant",
        "Strategic Storytelling Lead",
        "Career Messaging Advisor",
        "Qualifications Branding Partner"
    ]
}


def generate_title(vibe: str = None, tier: int = None) -> str:
    """
    Generate a funny or brutally honest mock job title.

    Parameters:
        vibe (str, optional): One of 'tech', 'corporate', 'creative', 'burnout', or 'general'
        tier (int, optional): Ranges from 0 (unhinged) to 3 (plausibly professional)

    Returns:
        str: A generated fake-but-too-real job title
    """
    if tier is not None and tier in TIERED_TITLES:
        return random.choice(TIERED_TITLES[tier])

    if vibe and vibe in TITLE_CATEGORIES:
        return random.choice(TITLE_CATEGORIES[vibe])

    # Fallback to pulling from all categories
    all_titles = sum(TITLE_CATEGORIES.values(), [])
    return random.choice(all_titles)
