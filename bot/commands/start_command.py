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

    DATABASE_URL = context.bot_data['DATABASE_URL']

    user_manager = UserManager(DATABASE_URL)
    if not user_manager.user_exists(update.effective_user.id):
        user_manager.add_user(update.effective_user.id, update.effective_user.username)
        await update.message.reply_text("Successfully Registered.")