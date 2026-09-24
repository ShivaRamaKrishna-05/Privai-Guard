import logging
import uuid
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config import settings
from app.api.auth import router as auth_router
from app.api.privacy import router as privacy_router
from app.api.chat import router as chat_router
from app.api.policies import router as policies_router
from app.api.events import router as events_router
from app.api.admin import router as admin_router

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO),
                    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger("privai_guard")

app = FastAPI(title=settings.app_name, version="1.0.0",
              description="Privacy and security gateway for LLM applications.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE","OPTIONS"],
    allow_headers=["Authorization","Content-Type","X-Request-ID"],
)

@app.middleware("http")
async def request_context(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    request.state.request_id = request_id
    try:
        response = await call_next(request)
    except Exception:
        logger.exception("Unhandled error | request_id=%s", request_id)
        return JSONResponse(status_code=500,
            content={"error":"Internal server error","request_id":request_id})
    response.headers["X-Request-ID"] = request_id
    return response

@app.exception_handler(RequestValidationError)
async def validation_error(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422,
        content={"error":"Invalid request",
                 "request_id":getattr(request.state,"request_id","unknown")})

@app.get("/")
async def root():
    return {"status":"ok","service":"PrivAI Guard"}

@app.get(f"{settings.api_v1_prefix}/health")
async def health():
    return {"status":"ok","service":"PrivAI Guard"}

app.include_router(auth_router, prefix=f"{settings.api_v1_prefix}/auth")
app.include_router(privacy_router, prefix=f"{settings.api_v1_prefix}/privacy")
app.include_router(chat_router, prefix=settings.api_v1_prefix)
app.include_router(policies_router, prefix=f"{settings.api_v1_prefix}/policies")
app.include_router(events_router, prefix=f"{settings.api_v1_prefix}/events")
app.include_router(admin_router, prefix=f"{settings.api_v1_prefix}/admin")
