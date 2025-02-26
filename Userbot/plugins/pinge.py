################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
import random
################################################################
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping

from Userbot import nlx
from Userbot.helper.database import dB
from Userbot.helper.tools import (Emojik, get_time, initial_ctext, ky,
                                  start_time)


@ky.ubot("ping")
@ky.devs("cping")
@ky.deve("cping")
async def ping_(c, m, _):
    em = Emojik(c)
    em.initialize()
    start = datetime.now()
    await c.invoke(Ping(ping_id=0))
    end = datetime.now()
    upnya = await get_time((time() - start_time))
    duration = round((end - start).microseconds / 100000, 2)
    pong_, uptime_, owner_, ubot_, proses_, sukses_ = initial_ctext(c)
    _ping = f"""
<b>{em.ping}{pong_}:</b> <u>{duration}ms</u>
<b>{em.pong}{uptime_}:</b> <u>{upnya}</u>
<b>{em.owner}{owner_}</b>"""
    return await m.reply(_ping)


def add_absen(c, text):
    auto_text = dB.get_var(c.me.id, "TEXT_ABSEN") or []
    auto_text.append(text)
    dB.set_var(c.me.id, "TEXT_ABSEN", auto_text)


@ky.deve("absen")
@ky.devs("absen")
async def _(c: nlx, message, _):
    txt = dB.get_var(c.me.id, "TEXT_ABSEN")
    if len(message.command) == 1:
        if not txt:
            return
        try:
            psn = random.choice(txt)
            return await message.reply(psn)
        except:
            pass
    else:
        command, variable = message.command[:2]
        if variable.lower() == "text":
            for x in nlx._ubot:
                value = " ".join(message.command[2:])
                add_absen(x, value)

        else:
            return
