# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved.


from pyrogram import __version__ as pyver
from pyrogram import idle
import heroku3
from pyrogram.errors import BadRequest
from config import PREFIX, LOG_CHAT, HEROKU_API, HEROKU_APP_NAME
from Stuf import app

app.start()
me = app.get_me()

print(
    f"Stuf UserBot started for user {me.first_name}. Type {PREFIX}help in any telegram chat."
)
print(
    f"Stuf UserBot started for user {me.first_name}. Type {PREFIX}help in any telegram chat."
)
try:
    if not str(LOG_CHAT).startswith("-100"):
        stuf = app.create_supergroup("Stuf-Logs", "Powered by : @stufgrup")
        app.set_chat_photo(stuf.id, photo="Stuf/dll/stuf.png")
        Heroku = heroku3.from_key(HEROKU_API)
        her = Heroku.app(HEROKU_APP_NAME)
        heroku_var = her.config()
        heroku_var["LOG_CHAT"] = stuf.id
    else:
        print("LOG_CHAT, Sudah benar")
    app.send_message(
        LOG_CHAT,
        f"🔥 **𝗦𝘁𝘂𝗳-𝗨𝘀𝗲𝗿𝗕𝗼𝘁 𝘂𝗱𝗮𝗵 𝗮𝗸𝘁𝗶𝗳** 🔥\n└ •**ᴏᴡɴᴇʀ** : [{me.first_name}](tg://user?id={me.id})\n└ •**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyver}`\n└ •**ꜱᴛᴜꜰ ᴠᴇʀsɪᴏɴ  :** `0.0.1`\n└ •**sᴜᴘᴘᴏʀᴛ ʙʏ :** @stufgrup\n\n└ •**ᴄʜᴀɴɴᴇʟ:** @stufuserbot\n\n**Gunakan** `{PREFIX}ping` **untuk cek bot aktif**"
    )
    app.join_chat("stufgrup")
    app.join_chat("stufchannel")
    app.join_chat("stufuserbot")
    
    idle()
except BadRequest:
    pass
