import asyncio
# import uvloop
from aiohttp import web
from pyrogram import idle
from pyrogram.errors import FloodWait

from app import client
from app.web_server import app
from app.config import Config, logger

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()

async def main_process():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=Config.PORT)
    await site.start()
    
    while True:
        try:
            await client.start()
            await idle()
        except FloodWait as e:
            logger.critical(f"FloodWait Error: Waiting for {e.value} seconds before resuming")
            await asyncio.sleep(e.value)
        except (KeyboardInterrupt, SystemExit):
            logger.info("Shutting down Pyrogram client and server gracefully.")
            await runner.cleanup()
            await client.stop()
            break


# loop.run_until_complete(main_process())
asyncio.run(main_process())