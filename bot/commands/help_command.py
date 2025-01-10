from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /help command."""
    help_message = (
        "🛠 **Help Menu**\n\n"
        "Here’s a guide to all the commands you can use:\n\n"
        "📋 **Basic Commands:**\n"
        "- `/start` - Start the bot and see an overview of its features.\n"
        "- `/help` - Get detailed instructions for using the bot.\n\n"
        "👜 **Wallet Management:**\n"
        "- `/add <wallet_address>` - Add a Solana wallet to your tracking list. Replace `<wallet_address>` with the wallet's public key.\n"
        "- `/remove <wallet_address>` - Remove a Solana wallet from your tracking list.\n"
        "- `/list` - View all the Solana wallets you are currently tracking.\n\n"
        "🔔 **Notifications:**\n"
        "The bot will notify you about the following events:\n"
        "- Incoming transactions\n"
        "- Outgoing transactions\n"
        "- Large transfers (customizable thresholds in future updates).\n\n"
        "💡 **Usage Tips:**\n"
        "- Ensure wallet addresses are valid Solana public keys before adding them.\n"
        "- You can track multiple wallets at once.\n"
        "- Use `/list` to manage your tracked wallets effectively.\n\n"
        "Need more help? Contact us at [support@example.com]."
    )
    await update.message.reply_text(help_message, parse_mode="Markdown")
