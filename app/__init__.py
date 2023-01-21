import logging
# import uvloop
from pyrogram import Client

from app.bot import Bot
from app.config import Config, logger

logger.setLevel(logging.DEBUG)
logging.basicConfig(
    format="[%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] %(message)s"
)

client = Bot()

"""
client = Client(
    "pyrogram",
    in_memory=True,
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=Config.WORKERS,
    plugins={
        "root": "app/plugins"
    }
)
"""