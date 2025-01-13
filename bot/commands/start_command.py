"""
This module contains the implementation of the /start command for a Telegram bot.
The /start command is handled by the `start_command` function, which sends a welcome message
to the user and registers the user in the database if they do not already exist.
Functions:
    - start_command(update: Update, context: ContextTypes.DEFAULT_TYPE): Handles the /start command.
"""

from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes
from ..user_manager import UserManager

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    message_path = Path(__file__).parent.parent / "messages" / "start.md"
    with open(message_path, "r", encoding="utf-8") as f:
        welcome_message = f.read()
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

    database_url = context.bot_data['database_url']

    user_manager = UserManager(database_url)
    if not user_manager.user_exists(update.effective_user.id):
        user_manager.add_user(update.effective_user.id, update.effective_user.username)
        await update.message.reply_text("Successfully Registered.")
