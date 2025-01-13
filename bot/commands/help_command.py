"""
This module contains the command handler for the /help command in a Telegram bot.
Functions:
    help_command(update: Update): Asynchronously handles the /help command by 
    reading the help message from a markdown file and sending it as a reply to the user.
"""

from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /help command."""
    message_path = Path(__file__).parent.parent / "messages" / "help.md"
    with open(message_path, "r", encoding="utf-8") as f:
        help_message = f.read()
    await update.message.reply_text(help_message, parse_mode="Markdown")
