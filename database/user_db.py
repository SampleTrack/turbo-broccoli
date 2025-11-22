import motor.motor_asyncio
from config import Config

class UserDatabase:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_URL)
        self.db = self.client[Config.DB_NAME]
        self.col = self.db.users

    async def add_user(self, user_id):
        if not await self.is_user_exist(user_id):
            await self.col.insert_one({"user_id": user_id, "banned": False})

    async def is_user_exist(self, user_id):
        return bool(await self.col.find_one({"user_id": user_id}))

    async def total_users_count(self):
        return await self.col.count_documents({})

    async def ban_user(self, user_id):
        await self.col.update_one({"user_id": user_id}, {"$set": {"banned": True}})

    async def remove_ban(self, user_id):
        await self.col.update_one({"user_id": user_id}, {"$set": {"banned": False}})

    async def get_ban_status(self, user_id):
        user = await self.col.find_one({"user_id": user_id})
        return user.get("banned", False) if user else False

    async def get_all_users(self):
        return self.col.find({})

user_db = UserDatabase()
