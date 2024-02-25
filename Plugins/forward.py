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

from pyrogram import Client, filters
import time

# Initialize the Pyrogram client

group_id = -1001991820558  # Replace with your group ID
notification_chat_id = -1001991820558  # Replace with the chat ID where you want to receive notifications


# Function to remove members from the group
def remove_members(bot, update, members_to_remove):
    total_removed = 0
    try:
        for member in members_to_remove:
            if member.user.is_bot:
                continue  # Skip bots
            try:
                bot.kick_chat_member(group_id, member.user.id)
                total_removed += 1
                # Notify after every 500 members removed
                if total_removed % 500 == 0:
                    bot.send_message(notification_chat_id, f"500 members removed. Total removed: {total_removed}")
                    time.sleep(1)  # Add a small delay to avoid rate limiting
            except Exception as e:
                continue  # Ignore errors and proceed to the next member
        bot.send_message(notification_chat_id, f"All members have been removed from the group. Total removed: {total_removed}")
    except Exception as e:
        bot.send_message(notification_chat_id, f"An error occurred: {e}")

# Command to start the bot
@app.on_message(filters.command("start"))
def start(bot, update):
    bot.send_message(update.chat.id, "Bot is ready. Use /play command to remove all members from the group.")

# Command to remove all members from the group
@app.on_message(filters.command("play") & filters.group & filters.user("me"))
def remove_all_members(bot, update):
    try:
        # Get all members in the group
        members = bot.get_chat_members(group_id)
        remove_members(bot, update, members)
    except Exception as e:
        bot.send_message(notification_chat_id, f"An error occurred: {e}")

# Run the bot
