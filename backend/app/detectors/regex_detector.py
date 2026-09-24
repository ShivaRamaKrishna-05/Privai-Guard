import re

PATTERNS = [
    ("EMAIL", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I), 0.99),
    ("PHONE", re.compile(r"(?<!\d)(?:\+?\d[\d ()-]{7,}\d)(?!\d)"), 0.92),
    ("IP_ADDRESS", re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b"), 0.99),
    ("CREDIT_CARD", re.compile(r"\b(?:\d[ -]*?){13,19}\b"), 0.95),    
    ("URL", re.compile(r"\bhttps?://[^\s]+", re.I), 0.98),
    ("GOVERNMENT_ID", re.compile(r"\b[A-Z]{2,5}[ -]?\d{6,12}\b", re.I), 0.72),
    ("ACCOUNT_NUMBER", re.compile(r"\b(?:account|a/c|acct)\s*(?:no\.?|number)?\s*[:#-]?\s*\d{6,18}\b", re.I), 0.90),
]

def detect(text: str):
    results = []
    for entity_type, pattern, confidence in PATTERNS:
        for m in pattern.finditer(text):
            results.append({"type":entity_type,"confidence":confidence,
                            "start":m.start(),"end":m.end(),"source":"regex"})
    return results
