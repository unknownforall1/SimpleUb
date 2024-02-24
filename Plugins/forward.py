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
from pyrogram.types import Message

# Define states
IMAGE, CAPTION, BUTTONS, CHAT_ID = range(4)

# Handler for /start command
@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hi! Welcome to the Promo Bot. Send /promo to create a promo message.")

# Handler for /promo command
@Client.on_message(filters.command("promo"))
async def promo_command(client, message):
    await message.reply_text("Please send the image for the promo message.")
    await set_state(message.chat.id, IMAGE)

# Handler for receiving the image
@Client.on_message(filters.photo & filters.private & filters.state(IMAGE))
async def receive_image(client, message):
    await message.download(f"image.jpg")
    await set_state(message.chat.id, CAPTION)
    await message.reply_text("Great! Now please provide the caption for the promo message.")

# Handler for receiving the caption
@Client.on_message(filters.text & filters.private & filters.state(CAPTION))
async def receive_caption(client, message):
    caption = message.text
    await set_user_data(message.chat.id, "caption", caption)
    await set_state(message.chat.id, BUTTONS)
    await message.reply_text("Now please provide the buttons format.")

# Handler for receiving the buttons format
@Client.on_message(filters.text & filters.private & filters.state(BUTTONS))
async def receive_buttons(client, message):
    buttons = message.text
    await set_user_data(message.chat.id, "buttons", buttons)
    await set_state(message.chat.id, CHAT_ID)
    await message.reply_text("Finally, please provide the channel or group ID where you want to send the promo message.")

# Handler for receiving the chat ID
@Client.on_message(filters.text & filters.private & filters.state(CHAT_ID))
async def receive_chat_id(client, message):
    chat_id = message.text
    await set_user_data(message.chat.id, "chat_id", chat_id)

    # Once all information is collected, send confirmation message
    confirmation_message = (
        f"Promo message:\n"
        f"Caption: {await get_user_data(message.chat.id, 'caption')}\n"
        f"Buttons: {await get_user_data(message.chat.id, 'buttons')}\n"
        f"Destination: {await get_user_data(message.chat.id, 'chat_id')}\n\n"
        "Everything is set! Send /send to send the promo message."
    )
    await message.reply_text(confirmation_message)

# Handler for /send command
@Client.on_message(filters.command("send"))
async def send_command(client, message):
    # Send the promo message with the collected information
    caption = await get_user_data(message.chat.id, "caption")
    buttons = await get_user_data(message.chat.id, "buttons")
    chat_id = await get_user_data(message.chat.id, "chat_id")

    # Here, you can use the collected information to send the promo message
    # For example:
    await client.send_photo(chat_id, photo="image.jpg", caption=caption, reply_markup=buttons)
    pass

async def set_state(chat_id, state):
    # Set the state for a specific chat ID
    pass

async def set_user_data(chat_id, key, value):
    # Set user data for a specific chat ID and key
    pass

async def get_user_data(chat_id, key):
    # Get user data for a specific chat ID and key
    pass

# Run the client
