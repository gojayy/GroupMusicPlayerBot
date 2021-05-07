from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEJwOBglMyU7frT-mByTBO5lQq2ZpD9ywACbxIAAlEOoEitB1o5LyEHaR8E")
    await message.reply_text(
        f"""Halo, saya adalah {bn}!
Saya adalah bot Music yang dirancang khusus untuk menemani anda memutar musik dalam grup melalui obrolan suara.
Masukkan saya kedalam grup, dan dengarkan musik sepuasnya!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ", url="https://telegra.ph/CARA-PENGGUNAAN-05-07")
                  ],[
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url="https://t.me/ifcksht"
                    ),
                    InlineKeyboardButton(
                        "ɪɴsᴛᴀɢʀᴀᴍ", url="https://www.instagram.com/arfrhmndani_/"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bot Musik Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ", url="https://telegra.ph/CARA-PENGGUNAAN-05-07")
                ]
            ]
        )
   )


