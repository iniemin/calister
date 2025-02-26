import asyncio

from pyrogram.errors import ChatWriteForbidden

from ..database import dB
from ._logs import Emojik
from ._misc import ReplyCheck


class AFK_:
    def __init__(self, client, message, reason=""):
        self.client = client
        self.message = message
        self.reason = reason
        self.emo = Emojik(self.client)
        self.emo.initialize()

    async def set_afk(self):
        rep = self.message.reply_to_message
        value = None
        gclog = self.client.get_logger(self.client.me.id)
        logs = gclog if gclog else "me"
        type_mapping = {
            "text": rep.text,
            "photo": rep.photo,
            "voice": rep.voice,
            "audio": rep.audio,
            "video": rep.video,
            "video_note": rep.video_note,
            "animation": rep.animation,
            "sticker": rep.sticker,
            "document": rep.document,
            "contact": rep.contact,
        }
        for media_type, media in type_mapping.items():
            if media:
                send = await rep.copy(logs)
                value = {
                    "type": media_type,
                    "message_id": send.id,
                }
                break
        if value:
            dB.set_var(self.client.me.id, "AFK", value)
        status = dB.get_var(self.client.me.id, "AFK")
        msg_status = await self.client.get_messages(logs, int(status["message_id"]))
        try:
            if msg_status:
                ae = await msg_status.copy(
                    self.message.chat.id, reply_to_message_id=ReplyCheck(self.message)
                )
                await asyncio.sleep(3)
                return await ae.delete()
            else:
                ae = await self.message.reply("Currently AFK!!")
                await asyncio.sleep(3)
                return await ae.delete()
        except ChatWriteForbidden:
            return
        except Exception as er:
            return await self.message.reply(f"{self.emo.gagal}**ERROR**: `{str(er)}`")

    async def get_afk(self):
        status = dB.get_var(self.client.me.id, "AFK")
        if not status:
            return
        gclog = self.client.get_logger(self.client.me.id)
        logs = gclog if gclog else "me"
        msg_status = await self.client.get_messages(logs, int(status["message_id"]))
        try:
            if msg_status:
                ae = await msg_status.copy(
                    self.message.chat.id, reply_to_message_id=ReplyCheck(self.message)
                )
                await asyncio.sleep(3)
                return await ae.delete()
            else:
                ae = await self.message.reply("Currently AFK!!")
                await asyncio.sleep(3)
                return await ae.delete()
        except ChatWriteForbidden:
            return
        except Exception as er:
            return await self.message.reply(f"{self.emo.gagal}**ERROR**: `{str(er)}`")

    async def unset_afk(self):
        gclog = self.client.get_logger(self.client.me.id)
        logs = gclog if gclog else "me"
        vars = dB.get_var(self.client.me.id, "AFK")
        if vars:
            await self.client.delete_messages(logs, int(vars["message_id"]))
            dB.remove_var(self.client.me.id, "AFK")
            afk_text = f"<b>{self.emo.sukses}Back to Online!!"
            try:
                ae = await self.message.reply(afk_text)
                await asyncio.sleep(3)
                return await ae.delete()
            except:
                return
