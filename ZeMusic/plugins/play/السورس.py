
import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/8733cf467f321f2ef767e.jpg",
        caption = f"""<b>  𝒘𝒆𝒍𝒄𝒐𝒎𝒆𝒖 𝒕𝒐 <b>\n<a href="https://t.me/zj_x3"> سورس بروتو 🥂</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "  𝒅𝒆𝒗 𝒔𝒐𝒖𝒓𝒄𝒆 ", url=f"https://t.me/B_0_R_U"),
                ],[
                    
                
                    InlineKeyboardButton(
                        " سورس بروتو🥂", url=f"https://t.me/zj_x3"),         
                ],

            ]

        ),

)
