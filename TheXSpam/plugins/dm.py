# ðªðððððððð ð©ð ð¨ððððð
# ð¨ðð ð¹ððððð ð¹ððððððð


from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
from TheXSpam import OneWord, RAID, ALTS
from config import SUDO_USERS
from random import choice


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      alt = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(alt) == 2:
          ok = await xspam.get_users(alt[1])
          id = ok.id

          if int(id) in ALTS:
                await e.reply_text(f"`á´ á´ÊÉªÒÉªá´á´ ÊÊ sÊÉªÉ´É´ÉªÉ´É¢ sá´á´á´ Êá´á´`")
          elif int(id) in SUDO_USERS:
                await e.reply_text(f"`á´ÊÉªs á´á´Êsá´É´ Éªs á´Ê sá´á´á´ á´sá´Ê`")
          else:
              counts = int(alt[0])
              print(counts)
              await e.reply_text("`á´á´ Êá´Éªá´ sá´á´Êá´á´á´ sá´á´á´á´ssÒá´ÊÊÊ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.01)

      elif e.reply_to_message and (len(alt) == 1):
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id

          if int(id) in ALTS:
                await e.reply_text(f"`á´ á´ÊÉªÒÉªá´á´ ÊÊ sÊÉªÉ´É´ÉªÉ´É¢ sá´á´á´ Êá´á´`")
          elif int(id) in SUDO_USERS:
                await e.reply_text(f"`á´ÊÉªs á´á´Êsá´É´ Éªs á´Ê sá´á´á´ á´sá´Ê`")
          else:
              counts = int(alt[0])
              await e.reply_text("`á´á´ Êá´Éªá´ sá´á´Êá´á´á´ sá´á´á´á´ssÒá´ÊÊÊ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.01)

      else:
            await e.reply_text("â¡ á´sá´É¢á´:\n   !dmraid 13 <Êá´á´ÊÊ á´á´ á´sá´Ê á´Ê á´sá´ÊÉ´á´á´á´>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], [".", "!", "/"]))
async def dmspam(client: Client, message: Message):
    alt = message.text.split(" ", 3)

    if  len(alt) == 4:
        quantity, uid, spam_text = int(alt[1]), alt[2], alt[3]

        if int(uid) in ALTS:
            await message.reply_text(f"`á´ á´ÊÉªÒÉªá´á´ ÊÊ á´Êá´Êá´É´ x`")
        elif int(uid) in SUDO_USERS:
            await message.reply_text(f"`á´ÊÉªs á´á´Êsá´É´ Éªs á´Ê sá´á´á´ á´sá´Ê`")
        else:
            await message.reply_text("`á´á´ ê±á´á´á´ sá´á´Êá´á´á´ sá´á´á´á´ssÒá´ÊÊÊ`")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(alt) == 3):
        id = message.reply_to_message.from_user.id
        quantity = int(alt[1])
        spam_text = alt[2]

        if int(id) in ALTS:
            await message.reply_text(f"`á´ á´ÊÉªÒÉªá´á´ ÊÊ sÊÉªÉ´É´ÉªÉ´É¢ sá´á´á´ x`")
        elif int(id) in SUDO_USERS:
            await message.reply_text(f"`á´ÊÉªs á´á´Êsá´É´ Éªs á´Ê sá´á´á´ á´sá´Ê`")
        else:
            await message.reply_text("`á´á´ ê±á´á´á´ sá´á´Êá´á´á´ sá´á´á´á´ssÒá´ÊÊÊ`")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text("ð á´sá´É¢á´:\n .dmspam 13 <á´ê±á´Ê Éªá´> Shinning spam\n .dmspam 13 shinng spam <Êá´á´ÊÊ á´á´ á´sá´Ê>")
