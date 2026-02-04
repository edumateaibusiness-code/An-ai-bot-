from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)
db = client[Config.DATABASE_NAME]
course_collection = db["courses"]

async def save_course_link(user_id, link_data):
    """Grup se mile course link ko save karne ke liye"""
    await course_collection.update_one(
        {"user_id": user_id},
        {"$set": {"link": link_data}},
        upsert=True
    )

async def get_user_course(user_id):
    return await course_collection.find_one({"user_id": user_id})
