# ðªðððððððð ð©ð ð¨ððððð
# ð¨ðð ð¹ððððð ð¹ððððððð

import os
import datetime

from TheXSpam import commandpro
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr


VERSION = 3.3

ALT = f"â sÊÉªÉ´É´ÉªÉ´É¢ sá´á´á´ â\n\n"
ALT += f"â  **á´Êá´Êá´É´ á´ á´ÊsÉªá´É´** : `3.10.4`\n"
ALT += f"â  **á´ÊÊá´ á´ á´ÊsÉªá´É´** : `{pyro_vr}`\n"
ALT += f"â  **sÊÉªÉ´É´ÉªÉ´É¢ sá´á´á´ á´ á´ÊsÉªá´É´**  : `{VERSION}`\n"
ALT += f"â  **á´á´á´á´á´á´ê±** : [Êá´á´¢á´á´ á´Êá´á´s](t.me/RazeeChats)\n"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"â sÊÉªÉ´É´ÉªÉ´É¢ sá´á´á´\nâ á´ÉªÉ´É¢: `{ms}ms`\nâ á´ á´ÊsÉªá´É´: `{VERSION}`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xspam: Client, e: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(e.chat.id, ALIVE_PIC, caption=ALT)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(e.chat.id, ALIVE_PIC, caption=ALT)


@Client.on_message(commandpro(["op", "nice", "cute", "hot", "!save", "x", "kid"]) & filters.me)
async def downloader(client: Client, message: Message):
    targetContent = message.reply_to_message
    load = await client.download_media(targetContent)
    await client.send_document("me", load)
    os.remove(load)
