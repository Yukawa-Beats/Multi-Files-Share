#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👤 Created By : <a href='https://t.me/ybdemochannel'>Yukawa Beats</a>\n\n📱 Instagram : <a href='https://instagram/yukawa_beats'>👉🏻 Tap It 👈🏻</a>\n\n🗣 Group : <a href='https://t.me/ybmoviesgroup'>YB MOVIES</a>\n\n⭕️ Channel : <a href='https://t.me/ybdemochannel'>YB Updates/a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
