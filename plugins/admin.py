from pyrogram import Client, filters
from database.user_db import user_db
from config import Config
import time

@Client.on_message(filters.command("log") & filters.user(Config.ADMIN_ID))
async def log_handler(client, message):
    # Simple log file sender
    try:
        await message.reply_document("log.txt") 
    except:
        await message.reply_text("Log file not found or empty.")

@Client.on_message(filters.command("ping"))
async def ping_handler(client, message):
    start_time = time.time()
    msg = await message.reply_text("Pinging...")
    end_time = time.time()
    await msg.edit_text(f"🏓 Pong! {round((end_time - start_time) * 1000)}ms")

@Client.on_message(filters.command("ban") & filters.user(Config.ADMIN_ID))
async def ban_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /ban [user_id]")
    try:
        user_id = int(message.command[1])
        await user_db.ban_user(user_id)
        await message.reply_text(f"User {user_id} banned.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

@Client.on_message(filters.command("unban") & filters.user(Config.ADMIN_ID))
async def unban_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /unban [user_id]")
    try:
        user_id = int(message.command[1])
        await user_db.remove_ban(user_id)
        await message.reply_text(f"User {user_id} unbanned.")
    except:
        await message.reply_text("Invalid ID.")

@Client.on_message(filters.command("users") & filters.user(Config.ADMIN_ID))
async def stats_handler(client, message):
    count = await user_db.total_users_count()
    await message.reply_text(f"📊 Total Users: {count}")
