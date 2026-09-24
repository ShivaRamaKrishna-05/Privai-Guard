from app.detectors.detector_manager import detect_all
from app.privacy.risk_engine import calculate_risk
from app.privacy.policy_engine import aggregate_action, DEFAULT_POLICIES
from app.privacy.anonymizer import sanitize

def analyze_text(text, policies=None):
    detections=detect_all(text)
    score,level=calculate_risk(detections,text)
    action=aggregate_action(detections,policies or DEFAULT_POLICIES)
    sanitized=sanitize(text,detections,policies or DEFAULT_POLICIES)
    return {"detections":detections,"risk_score":score,"risk_level":level,
            "action":action,"sanitized_text":sanitized,
            "detection_sources":sorted({d["source"] for d in detections})}
