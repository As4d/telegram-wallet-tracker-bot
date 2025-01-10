from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    message_path = Path(__file__).parent.parent / "messages" / "start.md"
    with open(message_path, "r", encoding="utf-8") as f:
        welcome_message = f.read()
    await update.message.reply_text(welcome_message, parse_mode="Markdown")
