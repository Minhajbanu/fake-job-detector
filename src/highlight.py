from src.scam_keywords import SCAM_KEYWORDS

def find_scam_keywords(text):
    text_lower = text.lower()
    found = []

    for word in SCAM_KEYWORDS:
        if word in text_lower:
            found.append(word)

    return list(set(found))
