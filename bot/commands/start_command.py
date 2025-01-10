from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    welcome_message = (
        "Welcome to Sol Wallet Tracker Bot! 🎉\n\n"
        "Here’s what I can do:\n"
        "- Track Solana wallet transactions in real-time.\n"
        "- Notify you about incoming and outgoing transactions.\n"
        "- Help you manage multiple wallet subscriptions.\n\n"
        "Use the following commands to get started:\n"
        "/help - Detailed usage instructions\n"
        "/add <wallet_address> - Add a wallet to track\n"
        "/remove <wallet_address> - Remove a tracked wallet\n"
        "/list - View all tracked wallets\n"
    )
    await update.message.reply_text(welcome_message)
