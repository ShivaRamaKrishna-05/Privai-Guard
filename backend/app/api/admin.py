from fastapi import APIRouter, Depends
from app.auth.dependencies import require_admin
from app.database.mongodb import events_collection

router=APIRouter(tags=["Admin"])

@router.get("/statistics")
async def statistics(user=Depends(require_admin)):
    return {
        "total_requests":await events_collection.count_documents({}),
        "blocked_requests":await events_collection.count_documents({"action":"BLOCK"}),
        "critical_requests":await events_collection.count_documents({"risk_level":"CRITICAL"}),
        "high_risk_requests":await events_collection.count_documents({"risk_level":"HIGH"}),
    }
