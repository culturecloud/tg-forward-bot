import pyromod.listen

from pyrogram import Client, __version__
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait

from app.config import Config, logger
from app.user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "pyrogram_bot",
            bot_token=Config.BOT_TOKEN,
            in_memory=True,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "app/plugins"
            },
            workers=Config.WORKERS
        )
        self.LOGGER = logger

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER.info(f"@{usr_bot_me.username} started!")
        self.USER, self.USER_ID = await User().start()
        self.LOGGER.info("User started!")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped. Bye.")
