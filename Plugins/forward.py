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
from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import pyfiglet

# Initialize the Pyrogram client

error_chat_id = "siddhant_devil"  # Change this to the username or ID of the user you want to forward error logs to

# Function to generate a Telegraph link for a file or media
from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import pyfiglet

# Initialize the Pyrogram client

error_chat_id = "siddhant_devil"  # Change this to the username or ID of the user you want to forward error logs to


# Function to generate a Telegraph link for a file or media
def generate_telegraph_link(file_path):
    try:
        # Upload the file to Telegraph
        response = upload_file(file_path)
        telegraph_url = response["url"]
        return telegraph_url
    except Exception as e:
        # Forward error logs to the specified user
        app.send_message(error_chat_id, f"Error generating Telegraph link: {e}")
        return None

# Command to start the bot
@app.on_message(filters.command("start"))
def start(bot, update):
    bot.send_message(update.chat.id, "Welcome! Send me any file, photo, or text to generate a Telegraph link or convert text into different fonts.")

# Handler for receiving files, photos, or media
@app.on_message(filters.document | filters.photo)
def receive_file(bot, update: Message):
    try:
        # Get the file path
        file_path = update.download()
        
        # Generate the Telegraph link
        telegraph_link = generate_telegraph_link(file_path)
        
        # Send the Telegraph link
        if telegraph_link:
            bot.send_message(update.chat.id, f"Here is the Telegraph link: {telegraph_link}")
        else:
            bot.send_message(update.chat.id, "Failed to generate Telegraph link.")
    except Exception as e:
        # Forward error logs to the specified user
        app.send_message(error_chat_id, f"Error receiving file: {e}")

# Handler for receiving text messages
@app.on_message(filters.text)
def receive_text(bot, update: Message):
    try:
        # Convert text into different fonts
        fonts = pyfiglet.FigletFont.getFonts()
        formatted_text = ""
        for font in fonts:
            formatted_text += f"<b>{font}</b>:\n"
            formatted_text += pyfiglet.figlet_format(update.text, font=font) + "\n\n"
        
        # Send the formatted text back to the user
        bot.send_message(update.chat.id, formatted_text, parse_mode="HTML")
    except Exception as e:
        # Forward error logs to the specified user
        app.send_message(error_chat_id, f"Error receiving text: {e}")

# Forward all messages from users to the specified user

