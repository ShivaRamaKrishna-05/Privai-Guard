from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.config import settings

def create_access_token(user_id: str, role: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_minutes)
    return jwt.encode({"sub":user_id,"role":role,"exp":expire},
                      settings.jwt_secret, algorithm=settings.jwt_algorithm)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except JWTError:
        return None
