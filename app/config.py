import os
import logging

class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "pyrogram_user")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    TIMEZONE = os.environ.get("TZ", "Asia/Kolkata")
    WORKERS = int(os.environ.get("WORKERS", "4"))
    PORT = int(os.environ.get("PORT", "80"))

logger = logging.getLogger(__name__)
