# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)


from pyrogram import filters, Client, enums
from bot import channelforward
from config import Config
from translation import Translation
import asyncio
import time
from pyrogram.errors import FloodWait



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



@channelforward.on_message((filters.channel) & (filters.document | filters.video ), group=4)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
            await message.chat_id
            func = message.copy
            await asyncio.sleep(2)
            await func(to_channel)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
   except Exception as e:
       logger.exception(e)
    
