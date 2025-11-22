from pyrogram import Client, filters
from script import Script
from database.user_db import user_db
from config import Config

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    if await user_db.get_ban_status(message.from_user.id):
        return
    await user_db.add_user(message.from_user.id)
    await message.reply_text(Script.START_TXT.format(message.from_user.first_name))

@Client.on_message(filters.command("help"))
async def help_handler(client, message):
    await message.reply_text(Script.HELP_TXT)

@Client.on_message(filters.command("about"))
async def about_handler(client, message):
    await message.reply_text(Script.ABOUT_TXT)

@Client.on_message(filters.command(["version", "changelog"]))
async def version_handler(client, message):
    txt = f"**v{Config.BOT_VERSION}**\n\n📝 Recent Updates:\n{Config.LAST_UPDATE}"
    await message.reply_text(txt)
