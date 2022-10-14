from pyrogram import Client, filters, idle
from config import *

if not API_ID:
    API_ID = int(input("ENTER API_ID: \n"))
if not API_HASH:
    API_HASH = input("ENTER API_HASH: \n")
if not BOT_TOKEN:
    BOT_TOKEN = input("ENTER BOT_TOKEN: \n")
if not MONGO_DB_URL:
    MONGO_DB_URL = input("ENTER MONGO_DB_URL: \n")
if not OWNER_ID:
    OWNER_ID = input("ENTER OWNER_ID: \n")

creamy = Client(":creamy:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@creamy.on_message(group=1)
async def chat_watcher(_, m):
    if str(m.chat.id)[0] == "-":
        await add_chat(m.chat.id)
        return
    else:
        await add_user(m.chat.id)
        return

async def broadcast(_, m):
    if not m.reply_to_message:
        query = m.text.split(None, 1)[1]
        if not query:
            return await m.reply("REPLY TO A MESSAGE OR ENTER SOME TEXT..!")
    
