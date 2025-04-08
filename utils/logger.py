import datetime
import json

# Event icons for fun + clarity (and they're cute)
EVENT_ICONS = {
    "info": "ℹ️",
    "debug": "🐛",
    "warning": "⚠️",
    "error": "❌",
    "success": "✅",
    "user": "👤",
    "style": "🎨",
    "buzzword": "💬"
}

def log_event(event_type: str, message: str, context: dict = None, log_to_file: bool = False):
    """
    Logs an event with a timestamp, message, optional context, and emoji icon.
    
    Parameters:
        event_type (str): Type/category of the event (e.g., 'info', 'error', 'user')
        message (str): Description of the event
        context (dict, optional): Additional structured metadata (e.g., user input, style used)
        log_to_file (bool): Whether to append the log to a file ('logs/events.log')
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    icon = EVENT_ICONS.get(event_type.lower(), "🔸")
    log_entry = {
        "timestamp": timestamp,
        "event": event_type.upper(),
        "icon": icon,
        "message": message,
        "context": context or {}
    }

    # Format for console/Streamlit printing
    pretty_message = f"{icon} [{timestamp}] {event_type.upper()}: {message}"
    if context:
        pretty_message += f" | Context: {json.dumps(context)}"

    print(pretty_message)

    # Optionally save to log file
    if log_to_file:
        with open("logs/events.log", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
