import asyncio
from pyrogram import Client, idle
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import Config
from plugins.web_server import web_server
from aiohttp import web
from database.db_manager import channel_db
from utils import get_motivation_content, get_random_riddle
import logging
import random

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Client(
    "AutoMotiveBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

scheduler = AsyncIOScheduler()

async def post_job():
    """The core job that runs periodically"""
    channels = await channel_db.get_all_channels()
    ad_text = await channel_db.get_ad()
    
    for ch in channels:
        try:
            # Logic: 80% chance motivation, 20% chance riddle (if enabled)
            is_riddle = ch.get('riddles', False) and random.random() < 0.2
            
            if is_riddle:
                q, a = await get_random_riddle()
                caption = f"🧩 **Riddle Time!**\n\n**Q:** {q}\n\n||**A:** {a}||\n\n#BrainTeaser"
                if ad_text:
                    caption += f"\n\n📢 {ad_text}"
                await bot.send_message(ch['chat_id'], caption)
            else:
                quote, img_url = await get_motivation_content()
                caption = f"{quote}\n\n#Motivation #DailyGrind"
                if ad_text:
                    caption += f"\n\n📢 {ad_text}"
                await bot.send_photo(ch['chat_id'], photo=img_url, caption=caption)
                
        except Exception as e:
            logger.error(f"Failed to send to {ch.get('chat_id')}: {e}")

async def start():
    await bot.start()
    logger.info("Bot Started!")
    
    # Start Web Server (Render requirement)
    app = await web_server()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", Config.PORT)
    await site.start()
    logger.info(f"Web Server running on port {Config.PORT}")

    # Start Scheduler (Runs job every 60 minutes - configurable in real production)
    scheduler.add_job(post_job, "interval", minutes=60)
    scheduler.start()
    
    await idle()
    await bot.stop()

if __name__ == "__main__":
    bot.run(start())
