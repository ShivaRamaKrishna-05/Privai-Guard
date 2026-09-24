import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings


async def test():
    try:
        client = AsyncIOMotorClient(
            settings.mongodb_uri,
            serverSelectionTimeoutMS=10000
        )

        await client.admin.command("ping")

        print("MONGODB CONNECTED")

        client.close()

    except Exception as e:
        print("MONGODB CONNECTION FAILED")
        print(type(e).__name__)
        print(e)


asyncio.run(test())