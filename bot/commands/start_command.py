from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    welcome_message = (
        "🌟 **Welcome to Sol Wallet Tracker Bot!**\n\n"
        "🔍 **Key Features:**\n"
        "- Track Solana wallet transactions in real-time\n"
        "- Receive instant notifications for transactions\n"
        "- Manage multiple wallet subscriptions\n\n"
        "🚀 **Getting Started:**\n"
        "- `/help` - View detailed usage instructions\n"
        "- `/add <wallet_address>` - Add a wallet to track\n"
        "- `/remove <wallet_address>` - Remove a tracked wallet\n"
        "- `/list` - View all tracked wallets\n\n"
        "Need assistance? Use `/help` for detailed instructions!"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")
