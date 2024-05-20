from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from Hellbot.functions.datas import MASTERS, ABUSE
from Hellbot.core.config import Config
from . import Config, HelpMenu, db, hellbot, on_message
import asyncio

@on_message("raid", allow_stan=True)
async def abuse(c: Client, m: Message):
    HELL = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(HELL) == 2:
        lee = await c.get_users(HELL[1])
        counts = int(HELL[0])
        for _ in range(counts):
            reply = choice(ABUSE)
            msg = f"[{lee.first_name}](tg://user?id={lee.id}) {reply}"
            await c.send_message(m.chat.id, msg)
            await asyncio.sleep(0.1)

    elif m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        lee = await c.get_users(user_id)
        counts = int(HELL[0])
        for _ in range(counts):
            reply = choice(ABUSE)
            msg = f"[{lee.first_name}](tg://user?id={lee.id}) {reply}"
            await c.send_message(m.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await m.reply_text(".raid 10 <reply to user or username>") 


HelpMenu("Raid").add(
    "raid abusive word on someone",
    "<reply> or <userid>",
    "To raid abusive words on replied user in present chat!",
    "raid @ForGo10God",
).info(
    "raid things!!"
).done()
