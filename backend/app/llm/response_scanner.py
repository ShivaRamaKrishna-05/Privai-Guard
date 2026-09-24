from app.detectors.detector_manager import detect_all
from app.privacy.policy_engine import aggregate_action
from app.privacy.anonymizer import sanitize

def scan_response(text):
    detections=detect_all(text)
    action=aggregate_action(detections)
    safe_text=sanitize(text,detections)
    if action=="BLOCK":
        safe_text="[Response blocked because it contained sensitive information.]"
    return detections,action,safe_text
