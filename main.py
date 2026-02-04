import os
import asyncio
import logging
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# Files se imports
from config import Config
from info import Info
from utils import get_readable_time, format_ai_response
from ai_logic import get_ai_response
from database import save_course_link

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- RENDER KEEP-ALIVE ---
app = Flask('')
@app.route('/')
def home(): return "EduMate.AI is Online! 🚀"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
# -------------------------

bot = Client(
    "EduMateBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(Info.START_MSG)

@bot.on_message(filters.command("about"))
async def about(client, message):
    await message.reply_text(Info.ABOUT_MSG)

@bot.on_message(filters.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'))
async def handle_links(client, message):
    await save_course_link(message.from_user.id, message.text)
    await message.reply_text("<b>✅ Course link saved in your EduMate database!</b>")

@bot.on_message(filters.text & ~filters.command(["start", "about", "help"]))
async def chat_ai(client, message):
    query = message.text # Maine yahan 'auerv' ko theek kar diya hai
    raw_response = get_ai_response(query)
    clean_response = format_ai_response(raw_response)
    await message.reply_text(f"<b>✨ EduMate AI:</b>\n\n{clean_response}")

if __name__ == "__main__":
    keep_alive()
    logger.info("EduMate.AI Bot is starting...")
    bot.run()
