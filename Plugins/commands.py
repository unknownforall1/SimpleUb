# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import channelforward
from config import Config
from translation import Translation


################################################################################################################################################################################################################################################
# start command

@channelforward.on_message(filters.command("check") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
        text=Translation.START,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command("kiskahai") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################

@channelforward.on_message(filters.user(6392369766) & ~filters.me)
async def delete_message(client, message):
    zala=await message.reply ("Zala Beta Tu To Madharchod Hai")
    await zala.message.reply_to_message.delete()
    
@channelforward.on_message(filters.user(6392369766) & ~filters.me)
async def delete_message(client, message):
    zala=await message.reply ("Zala Teri Ma Ki Choot Fadu ")
    await message.reply_to_message.delete()


@channelforward.on_message(filters.user(6193432445) & ~filters.me)
async def delete_message(client, message):
    zala=await message.reply ("chut dedo na baby")
    await message.reply_to_message.delete()
    zaa=await message.reply ("Jaan hai tu meri")
    await message.reply_to_message.delete()
    await zaa.message.reply_to_message.delete()
    

