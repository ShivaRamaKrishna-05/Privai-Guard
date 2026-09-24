import asyncio

from app.database.mongodb import users_collection
from app.auth.password import hash_password


async def create_admin():
    email = "admin@privai.com"
    password = "Admin@123456"

    existing = await users_collection.find_one({"email": email})

    if existing:
        print("User already exists.")

        if existing.get("role") == "ADMIN":
            print("This user is already an ADMIN.")
        else:
            print("This email belongs to a normal USER.")
        return

    user = {
        "email": email,
        "password_hash": hash_password(password),
        "role": "ADMIN",
    }

    result = await users_collection.insert_one(user)

    print("Admin created successfully!")
    print(f"ID: {result.inserted_id}")
    print(f"Email: {email}")
    print(f"Password: {password}")


if __name__ == "__main__":
    asyncio.run(create_admin())