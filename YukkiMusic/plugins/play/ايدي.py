import asyncio
import pyrogram
from pyrogram import Client, filters
from YukkiMusic import settingsApp
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj







#@app.on_message(command([""]) & filters.group &
#async def khalid(client: Client, message: Message):
    #usr = await client.get_users(message.from_user.id)
    #name = usr.first_name
    #async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    #await message.reply_photo(photo.file_id,       caption=f"""á´sá´Ê -âº {message.from_user.mention}\nððð²ð¿ð»ð®ðºð² -âº @{message.from_user.username}\nÉªá´ -âº {message.from_user.id}\nbio Â» {bio}""", 
        #reply_markup=InlineKeyboardMarkup(

            #[

                #[

                    #InlineKeyboardButton(

                        #name, url=f"https://t.me/{message.from_user.id}")

                #],

            #]

        #),

    #)

@app.on_message(filters.regex("^$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""â¢ In the end, you are the bad, and they are the innocent\n\nâ¢ ðµððð -âº {message.from_user.mention}\nâ¢ ð¼ððð -âº @{message.from_user.username}\nâ¢ ðºðððð -âº Developer Mira\nâ¢ ð©ðð -âº {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=2089102006)

                ],

            ]

        ),

    )

@app.on_message(filters.regex("^ÙÙÙÙÙ$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    bio = usr.bio
    await message.reply_video(
        video=f"https://telegra.ph/file/f12360f05eefd9399bd0b.mp4",
        caption=f"""â¢ In the end, you are the bad, and they are the innocent\n\nâ¢ ðµððð -âº {message.from_user.mention}\nâ¢ ð¼ððð -âº @{message.from_user.username}\nâ¢ ðºðððð -âº Developer Mira\nâ¢ ð©ðð -âº {bio}""",
        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=2089102006)

                ],

            ]

        ),

    )

@app.on_message(filters.command("Ø§ÙØ¯Ù Ø§ÙÙØ¬ÙÙØ¹Ø©", ["", "."]) & ~filters.edited)
async def mira(client: Client, message: Message):
    m_reply = await message.reply_text(f"ID chat** [`{message.chat.id}`]")
    await m_reply_text("")


#Ø§ÙØ³ÙØ±Ø³ - Ø§ÙÙØ·ÙØ±


@app.on_message(filters.regex("^Ø§ÙØ³ÙØ±Ø³$") & filters.group & ~filters.edited)
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/588d70e34b51710ae8dce.jpg",
        caption=f"""â§ ð¾ðððððð ð»ð ðºððððð ð´ððð âª\n\nâ¢ á´á´á´ á´Êá´á´á´Ê -âº @PsPsP\nâ¢ á´Êá´É´É´á´Ê á´ÉªÊá´ -âº @NvvvC\n\n**- ÙÙØªÙØµÙØ¨ Ø§Ù ÙÙØ§Ø³ØªÙØ³Ø§Ø± ØªÙØ§ØµÙ ÙØ¹ ÙØ·ÙØ± Ø§ÙØ³ÙØ±Ø³**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "ÙØ·ÙØ± Ø§ÙØ³ÙØ±Ø³", user_id=2089102006)
                ],[
                    InlineKeyboardButton(
                       "ØªØ­Ø¯ÙØ«Ø§Øª ÙÙØ±Ø§", url=f"https://t.me/NvvvC")
                
                 ],

            ]

        ),

    )


@app.on_message(filters.regex("^Ø§ÙÙØ·ÙØ±$") & filters.group & ~filters.edited)
async def aboutd5ev(client: Client, message: Message):
    usr = await client.get_chat(2089102006)
    name = usr.first_name
    bio = (await client.get_chat(2089102006)).bio
    async for photo in client.iter_profile_photos(2089102006, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- ð«ðððððððð ð»ð ð©ðð ð´ððð âª -âº @PsPsP\n\n- ð«ðððððððð'ð ð©ðð -âº {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=2089102006)
                ],
            ]
        ),
    )

