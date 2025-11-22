from pyrogram import Client, filters
from database.db_manager import channel_db
from config import Config

@Client.on_message(filters.command("setchannel") & filters.user(Config.ADMIN_ID))
async def set_channel(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /setchannel [CHANNEL_ID]")
    try:
        chat_id = int(message.command[1])
        # Default: 60 mins interval, riddles off
        await channel_db.update_channel(chat_id, interval=60, riddles=False)
        await message.reply(f"✅ Channel {chat_id} added/updated.")
    except ValueError:
        await message.reply("Invalid Channel ID.")

@Client.on_message(filters.command("enable_riddles") & filters.user(Config.ADMIN_ID))
async def toggle_riddles(client, message):
    if len(message.command) < 3:
        return await message.reply("Usage: /enable_riddles [CHANNEL_ID] [on/off]")
    chat_id = int(message.command[1])
    status = message.command[2].lower() == "on"
    await channel_db.update_channel(chat_id, riddles=status)
    await message.reply(f"Riddles for {chat_id} set to: {status}")

# Monetization Features
@Client.on_message(filters.command("set_ad") & filters.user(Config.ADMIN_ID))
async def set_ad_text(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /set_ad [Text/Link]")
    ad_text = message.text.split(" ", 1)[1]
    await channel_db.set_ad(ad_text)
    await message.reply("✅ Advertisement text updated.")
