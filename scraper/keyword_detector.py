EXPLOIT_KEYWORDS = [
    "exploited in the wild",
    "active exploitation",
    "actively exploited",
    "zero-day exploited",
    "observed exploitation"
]

def detect_exploit_status(text):
    text_lower = text.lower()
    for keyword in EXPLOIT_KEYWORDS:
        if keyword in text_lower:
            return "Exploited in the Wild"
    return "No active exploitation reported"
