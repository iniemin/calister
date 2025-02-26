from asyncio import gather

from httpx import AsyncClient, Timeout

from Userbot import aiohttpsession

fetch = AsyncClient(
    cookies={"_U": "1AuG0BFRHDZ9nT8DVtfZMF_-q3KyqWmbJQjW11jZCuUUMqQbn3mFdFIsvEcDmUoVONjxSsgcHQZLHZ4TBwBaM8uVfnCX7mIYRRc-2XKrJY0TYFWCGuoUWgAyaML2WXtww29rqu6cC8fYVyoDPvn91FuAbGupDw4_tXAW4v0ZQ06_HZQCZ-lLwDS0ao6vh9D5oe23QIk_kMZzwOYDdCCmkO0__CCi3_BuCThm68vEjFgieDk-1z1hf80EImy-jc-3k", "SRCHHPGUSR": "SRCHLANG=en&PV=10.0.0&DM=1&BRW=HTP&BRH=M&CW=899&CH=778&SCW=899&SCH=778&DPR=1.3&UTC=420&HV=1737690332&PRVCW=1454&PRVCH=778"},
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
    },
    timeout=Timeout(20),
)


BASE = "https://batbin.me/"

dev_paste = {
    "nekobin": {
        "URL": "https://nekobin.com/api/documents",
        "RAV": "result.key",
        "GAS": "https://github.com/nekobin/nekobin",
    },
    "pasty": {
        "URL": "https://pasty.lus.pm/api/v2/pastes",
        "HEADERS": {
            "User-Agent": "PyroGramBot/6.9",
            "Content-Type": "application/json",
        },
        "RAV": "id",
        "GAS": "https://github.com/lus/pasty",
        "AVDTS": "modificationToken",
    },
    "pasting": {
        "URL": "https://pasting.codes/api",
    },
}


async def get(url: str, *args, **kwargs):
    async with aiohttpsession.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def head(url: str, *args, **kwargs):
    async with aiohttpsession.head(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def post(url: str, *args, **kwargs):
    async with aiohttpsession.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def multiget(url: str, times: int, *args, **kwargs):
    return await gather(*[get(url, *args, **kwargs) for _ in range(times)])


async def multihead(url: str, times: int, *args, **kwargs):
    return await gather(*[head(url, *args, **kwargs) for _ in range(times)])


async def multipost(url: str, times: int, *args, **kwargs):
    return await gather(*[post(url, *args, **kwargs) for _ in range(times)])


async def resp_get(url: str, *args, **kwargs):
    return await aiohttpsession.get(url, *args, **kwargs)


async def resp_post(url: str, *args, **kwargs):
    return await aiohttpsession.post(url, *args, **kwargs)


async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]
