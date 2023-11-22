# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters, enums
from pyrogram.errors import FloodWait
from bot import channelforward
from config import Config 
xdchannel = -1002031514094
@channelforward.on_message(filters.channel | filters.private | filters.chat)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if 1 == int(from_channel):
            func = message.copy if Config.AS_COPY else message.forward
            await func(int(to_channel), Config.AS_COPY)
            await asyncio.sleep(10)
   except FloodWait as e:
            await asyncio.sleep(e.x)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(10)
   except Exception as e:
      logger.exception(e)

