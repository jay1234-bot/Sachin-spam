# ©️ @SACHIN_OWNER || @V_VIP_OWNER
from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("➻❥⏤͟͞ᴋʀɪsʜᴀɴ💸⎯ꨄ", "https://t.me/censored_politicss"),
        Button.url("ᴜsᴇʀʙᴏᴛ 🕸️", "https://t.me/cutieee_musicbot")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/+PC-rxWT0YD1jM2Q9"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/+PC-rxWT0YD1jM2Q9")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/+PC-rxWT0YD1jM2Q9")
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞‌‌‌‌★**\n**┆**\n**┊◍ ʜᴇʏ : [{event.sender.first_name}] **\n**┆◍ ɪ ᴀᴍ : [{bot_name}](tg://user?id={bot_id}) **\n**┊**\n**┆● ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `0.2`\n**┊● ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `8.2.5.1.01`\n**╰─────────────────────────**\n**──────────────────────────**\n**⦿ Oᴡɴᴇʀ - [➻❥⏤͟͞ᴋʀɪsʜᴀɴ💸⎯ꨄ](https://t.me/censored_politicss) | [➻❥⏤͟͞ᴋʀɪsʜᴀɴ💸⎯ꨄ](https://t.me/censored_krishan) **\n**──────────────────────────**\n**    ❖ Uᴘᴅᴀᴛᴇ's ⏤͟͟͞͞‌‌‌‌ [𝚅𝙸𝙱𝙴𝚂 𝙷𝚄𝙱](https://t.me/+PC-rxWT0YD1jM2Q9) **\n**──────────────────────────**"
        await event.client.send_file(
                    event.chat_id,  
                    "https://pub-404d3d1646bf4caab306e0c1451fe7f9.r2.dev/photo_2024-12-26_19-48-24.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
