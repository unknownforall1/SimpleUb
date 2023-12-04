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

@channelforward.on_message(filters.user(5962777512) & filters.group)
async def delete_user_message(client, message):
    tera=await message.reply("shutup bitch")
    await message.delete()
    await tera.reply_to_message.delete()
    await asyncio.sleep(10)
    await message.delete()
    await tera.reply_to_message.delete()
    await tera.delete()

@channelforward.on_message((filters.private | filters.channel | filters.group) & (filters.document | filters.video ), group=4)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if int(to_channel) == int(to_channel):
            func = message.copy
            await asyncio.sleep(2)
            await func(int(to_channel))
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
   except Exception as e:
       logger.exception(e)

#@channelforward.on_message((filters.group) & filters.text & filters.incoming)
#async def delete_message(client, message):
  #  await asyncio.sleep(302)
   # await message.delete()
 #   saif=await message.reply ("............")
   # await saif.delete(302)
   # await saif.reply_to_message.delete()
 #   await asyncio.sleep(302)
   # await message.reply_to_message.delete()

