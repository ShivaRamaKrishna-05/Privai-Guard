from app.privacy.sanitizer import analyze_text

def test_email_anonymization():
    r=analyze_text("Contact test@example.com")
    assert any(d["type"]=="EMAIL" for d in r["detections"])
    assert "[EMAIL_1]" in r["sanitized_text"]

def test_credit_card_is_blocked():
    r=analyze_text("card 4111 1111 1111 1111")
    assert r["action"]=="BLOCK"
    assert "[REDACTED]" in r["sanitized_text"]

def test_clean_text():
    r=analyze_text("Tell me about Python.")
    assert r["detections"]==[]
    assert r["action"]=="ALLOW"
