from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.mongodb_uri)
db = client[settings.mongodb_db]
users_collection = db["users"]
events_collection = db["privacy_events"]
policies_collection = db["policies"]
requests_collection = db["api_requests"]

async def ping_db():
    try:
        await client.admin.command("ping")
        return True
    except Exception:
        return False
