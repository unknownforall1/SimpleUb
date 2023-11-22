# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if int(to_channel) == int(to_channel):
            func = message.copy
            await asyncio.sleep(1)
            await func(int(to_channel))
            await client.sleep(10)
            await asyncio.sleep(25)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(7)
   except Exception as e:
      logger.exception(e)
