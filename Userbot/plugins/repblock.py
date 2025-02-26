from Userbot import nlx
from Userbot.helper.tools import Emojik, ky


@ky.nocmd("REP_BLOCK", nlx)
async def _(client, message, _):
    em = Emojik(client)
    em.initialize()
    return await message.reply_text(
        f"{em.block}**Ga usah reply apalagi tag gw, lu udah block gua anak KONTOL!!**"
    )
