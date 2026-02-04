import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    MONGO_URI = os.environ.get("MONGO_URI", "")
    SAMBA_NOVA_API_KEY = os.environ.get("SAMBA_NOVA_API_KEY", "")
    DATABASE_NAME = "EduMate_DB"
