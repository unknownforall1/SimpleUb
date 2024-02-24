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


# Define a handler for the image message
@app.on_message(filters.photo)
async def handle_image(client, message):
    # Save the image
    await message.download(file_name="promo_image.jpg")
    # Ask for caption
    await message.reply_text("Please enter the caption for the promo:")

# Define a handler for the caption message
@app.on_message(filters.text & ~filters.command)
async def handle_caption(client, message):
    caption = message.text
    # Ask for buttons format
    await message.reply_text("Please enter the buttons format (e.g., [['Button 1', 'Button 2'], ['Button 3']]):")

# Define a handler for the buttons message
@app.on_message(filters.text & ~filters.command)
async def handle_buttons(client, message):
    buttons_format = eval(message.text)
    # Ask for channel or group id
    await message.reply_text("Please enter the channel or group id where you want to send the promo message:")

# Define a handler for the channel id message
@app.on_message(filters.text & ~filters.command)
async def handle_channel_id(client, message):
    channel_id = message.text
    # Send the promo message with media, caption, and buttons
    await client.send_photo(chat_id=channel_id, photo="promo_image.jpg", caption="Your caption here", reply_markup=InlineKeyboardMarkup(buttons_format))
    await message.reply_text("Everything is done! You can now send /send to send the promo message.")

# Define a handler for the /send command
@app.on_message(filters.command("send"))
async def send_command(client, message):
    await message.reply_text("Sending the promo message...")

# Run the bo
