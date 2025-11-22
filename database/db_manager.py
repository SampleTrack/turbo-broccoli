import motor.motor_asyncio
from config import Config

class ChannelDatabase:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_URL)
        self.db = self.client[Config.DB_NAME]
        self.col = self.db.channels

    async def update_channel(self, chat_id, interval=60, riddles=False):
        await self.col.update_one(
            {"chat_id": chat_id},
            {"$set": {"interval": interval, "riddles": riddles}},
            upsert=True
        )
    
    async def set_ad(self, ad_text):
        # We store ads in a specific config document
        await self.db.settings.update_one(
            {"type": "global_ad"},
            {"$set": {"text": ad_text}},
            upsert=True
        )

    async def get_ad(self):
        doc = await self.db.settings.find_one({"type": "global_ad"})
        return doc['text'] if doc else None

    async def get_all_channels(self):
        # Returns a list of all configured channels
        cursor = self.col.find({})
        return await cursor.to_list(length=None)

channel_db = ChannelDatabase()
