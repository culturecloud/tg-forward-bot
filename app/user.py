from pyrogram import Client, __version__
from app.config import Config, logger

BOT_USERNAME=Config.BOT_USERNAME

class User(Client):
    def __init__(self):
        super().__init__(
            "pyrogram_user",
            session_string=Config.SESSION,
            in_memory=True,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            workers=Config.WORKERS
        )
        self.LOGGER = logger

    async def start(self):
        await super().start()
        if BOT_USERNAME:
            await User.send_message(self, chat_id=BOT_USERNAME, text="/forward")
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("User stopped. Bye.")
