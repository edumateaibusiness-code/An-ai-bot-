from pyrogram import Client, filters
from config import Config
from ai_logic import get_ai_response
from database import save_course_link
import asyncio

bot = Client("AIBot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("<b>🤖 Welcome! I am your SambaNova Powered AI Bot.</b>\nSend me a course link or ask any question!")

@bot.on_message(filters.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'))
async def handle_links(client, message):
    # Agar user koi link bhejta hai
    await save_course_link(message.from_user.id, message.text)
    await message.reply_text("<b>✅ Course link saved in MongoDB!</b>")

@bot.on_message(filters.text & ~filters.command(["start"]))
async def chat_ai(client, message):
    query = message.text
    response = get_ai_response(query)
    await message.reply_text(f"<b>✨ AI Response:</b>\n\n{response}")

if __name__ == "__main__":
    bot.run()
