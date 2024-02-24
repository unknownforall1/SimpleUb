# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import logging
logger = logging.getLogger(__name__)

import asyncio
import time
from pyrogram import filters, Client, enums
from bot import channelforward as app
from pyrogram.errors import FloodWait
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Define states
IMAGE, CAPTION, BUTTONS, CHAT_ID = range(4)
user_data = {}

# Handler for /start command
@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hi! Welcome to the Promo Bot. Send /promo to create a promo message.")

# Handler for /promo command
@Client.on_message(filters.command("promo"))
async def promo_command(client, message):
    user_data[message.chat.id] = {"state": IMAGE}
    await message.reply_text("Please send the image for the promo message.")

# Handler for receiving the image
@Client.on_message(filters.photo & filters.private)
async def receive_image(client, message):
    if message.chat.id in user_data and user_data[message.chat.id]["state"] == IMAGE:
        await message.download(f"image.jpg")
        user_data[message.chat.id]["state"] = CAPTION
        await message.reply_text("Great! Now please provide the caption for the promo message.")
    else:
        await message.reply_text("Please start the promo process by sending /promo command.")

# Handler for receiving the caption
@Client.on_message(filters.text & filters.private)
async def receive_caption(client, message):
    if message.chat.id in user_data and user_data[message.chat.id]["state"] == CAPTION:
        user_data[message.chat.id]["caption"] = message.text
        user_data[message.chat.id]["state"] = BUTTONS
        await message.reply_text("Now please provide the buttons format.")
    else:
        await message.reply_text("Please start the promo process by sending /promo command.")

# Handler for receiving the buttons format
@Client.on_message(filters.text & filters.private)
async def receive_buttons(client, message):
    if message.chat.id in user_data and user_data[message.chat.id]["state"] == BUTTONS:
        user_data[message.chat.id]["buttons"] = message.text
        user_data[message.chat.id]["state"] = CHAT_ID
        await message.reply_text("Finally, please provide the channel or group ID where you want to send the promo message.")
    else:
        await message.reply_text("Please start the promo process by sending /promo command.")

# Handler for receiving the chat ID
@Client.on_message(filters.text & filters.private)
async def receive_chat_id(client, message):
    if message.chat.id in user_data and user_data[message.chat.id]["state"] == CHAT_ID:
        user_data[message.chat.id]["chat_id"] = message.text

        # Once all information is collected, send confirmation message
        confirmation_message = (
            f"Promo message:\n"
            f"Caption: {user_data[message.chat.id]['caption']}\n"
            f"Buttons: {user_data[message.chat.id]['buttons']}\n"
            f"Destination: {user_data[message.chat.id]['chat_id']}\n\n"
            "Everything is set! Send /send to send the promo message."
        )
        await message.reply_text(confirmation_message)
    else:
        await message.reply_text("Please start the promo process by sending /promo command.")

# Handler for /send command
@Client.on_message(filters.command("send"))
async def send_command(client, message):
    if message.chat.id in user_data:
        # Send the promo message with the collected information
        caption = user_data[message.chat.id]["caption"]
        buttons = user_data[message.chat.id]["buttons"]
        chat_id = user_data[message.chat.id]["chat_id"]

        # Here, you can use the collected information to send the promo message
        # For example:
        # await client.send_photo(chat_id, photo="image.jpg", caption=caption, reply_markup=buttons)
        pass
    else:
        await message.reply_text("Please start the promo process by sending /promo command.")

# Run the cl
