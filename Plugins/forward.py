# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import logging
logger = logging.getLogger(__name__)

import asyncio
import time
from pyrogram import filters, Client, enums
from bot import channelforward
from pyrogram.errors import FloodWait
from config import Config

@channelforward.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if int(to_channel) == int(to_channel):
            func = message.copy
            await asyncio.sleep(7)
            await func(int(to_channel))
            time.sleep(5)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
   except FloodWait as e:
       time.sleep(e.x)
   except Exception as e:
       logger.exception(e)

@channelforward.on_message((filters.group | filters.private) & filters.text & filters.incoming)
async def delete_message(client, message):
    await asyncio.sleep(3)
    saif=await message.reply ("wowww")
    await saif.reply_to_message.delete()
    await asyncio.sleep(1)
    await saif.delete()
    await message.reply_to_message.delete()

