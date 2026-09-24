from fastapi import APIRouter, Depends
from app.auth.dependencies import current_user
from app.database.mongodb import events_collection

router=APIRouter(tags=["Events"])

@router.get("")
async def events(user=Depends(current_user),limit:int=50):
    docs=[]
    cursor=events_collection.find({"user_id":user["sub"]}).sort("timestamp",-1).limit(min(limit,100))
    async for d in cursor:
        d.pop("_id",None)
        docs.append(d)
    return docs

@router.get("/{event_id}")
async def event(event_id:str,user=Depends(current_user)):
    d=await events_collection.find_one({"event_id":event_id,"user_id":user["sub"]},{"_id":0})
    return d or {"error":"Event not found"}
