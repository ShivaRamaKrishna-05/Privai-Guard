from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserResponse
from app.database.mongodb import users_collection
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.auth.dependencies import current_user

router=APIRouter(tags=["Authentication"])

@router.post("/register",response_model=UserResponse)
async def register(data:RegisterRequest):
    existing=await users_collection.find_one({"email":data.email.lower()})
    if existing: raise HTTPException(409,"Email already registered")
    doc={"email":data.email.lower(),"password_hash":hash_password(data.password),"role":"USER"}
    result=await users_collection.insert_one(doc)
    return {"id":str(result.inserted_id),"email":doc["email"],"role":doc["role"]}

@router.post("/login",response_model=TokenResponse)
async def login(data:LoginRequest):
    user=await users_collection.find_one({"email":data.email.lower()})
    if not user or not verify_password(data.password,user["password_hash"]):
        raise HTTPException(401,"Invalid credentials")
    return {"access_token":create_access_token(str(user["_id"]),user["role"]),"token_type":"bearer"}

@router.get("/me")
async def me(user=Depends(current_user)):
    return {"id":user["sub"],"role":user["role"]}
