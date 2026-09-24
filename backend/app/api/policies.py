from fastapi import APIRouter, Depends, HTTPException
from app.auth.dependencies import require_admin
from app.database.mongodb import policies_collection
from app.privacy.policy_engine import DEFAULT_POLICIES

router=APIRouter(tags=["Policies"])

@router.get("")
async def list_policies(user=Depends(require_admin)):
    custom={}
    async for p in policies_collection.find({}):
        custom[p["type"]]=p["action"]
    merged={**DEFAULT_POLICIES,**custom}
    return [{"type":k,"action":v} for k,v in merged.items()]

@router.put("/{entity_type}")
async def update_policy(entity_type:str,body:dict,user=Depends(require_admin)):
    action=body.get("action")
    if action not in {"ALLOW","WARN","MASK","ANONYMIZE","BLOCK"}:
        raise HTTPException(400,"Invalid policy action")
    await policies_collection.update_one({"type":entity_type},
        {"$set":{"type":entity_type,"action":action}},upsert=True)
    return {"type":entity_type,"action":action}
