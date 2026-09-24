from datetime import datetime, timezone
from uuid import uuid4

def now():
    return datetime.now(timezone.utc)

def event_document(user_id, request_id, detections, risk_score, risk_level, action):
    return {
        "event_id": str(uuid4()),
        "user_id": user_id,
        "request_id": request_id,
        "categories": sorted({d["type"] for d in detections}),
        "risk_score": risk_score,
        "risk_level": risk_level,
        "action": action,
        "timestamp": now(),
    }
