from Userbot import nlx
from Userbot.helper.tools import AFK_, capture_err, h_s, ky

__MODULES__ = "Afk"


def help_string(org):
    return h_s(org, "help_afk")


@ky.ubot("afk")
async def _(client: nlx, message, _):
    rep = message.reply_to_message
    if not rep:
        return await message.reply("Please reply to message!!")
    reason = client.get_arg(message)
    afk_handler = AFK_(client, message, reason)
    return await afk_handler.set_afk()


@ky.nocmd("AFK", nlx)
@capture_err
async def _(client, message, _):
    afk_handler = AFK_(client, message)
    return await afk_handler.get_afk()


@ky.ubot("unafk")
async def _(client, message, _):
    afk_handler = AFK_(client, message)
    return await afk_handler.unset_afk()
