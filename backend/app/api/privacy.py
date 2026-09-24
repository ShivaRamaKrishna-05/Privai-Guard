from fastapi import APIRouter, Depends
from app.schemas.privacy import AnalyzeRequest, AnalysisResponse
from app.privacy.sanitizer import analyze_text
from app.auth.dependencies import current_user
from app.database.mongodb import events_collection
from app.database.models import event_document

router=APIRouter(tags=["Privacy"])

@router.post("/analyze",response_model=AnalysisResponse)
async def analyze(data:AnalyzeRequest,user=Depends(current_user)):
    result=analyze_text(data.text)
    await events_collection.insert_one(event_document(
        user["sub"],"privacy-analysis",result["detections"],
        result["risk_score"],result["risk_level"],result["action"]))
    return result

@router.post("/sanitize")
async def sanitize_endpoint(data:AnalyzeRequest,user=Depends(current_user)):
    result=analyze_text(data.text)
    return {"sanitized_text":result["sanitized_text"],
            "risk_score":result["risk_score"],
            "risk_level":result["risk_level"],
            "action":result["action"]}
