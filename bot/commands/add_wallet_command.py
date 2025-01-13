from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes
from bot.wallet_manager import WalletManager
from ..user_manager import UserManager

async def add_wallet_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /add command."""
    wallet_address = context.args[0] if context.args else None
    if not wallet_address:
        message_path = Path(__file__).parent.parent / "messages" / "add.md"
        with open(message_path, "r", encoding="utf-8") as f:
            help_message = f.read()
        await update.message.reply_text(help_message, parse_mode="Markdown")
        return
        

    DATABASE_URL = context.bot_data['DATABASE_URL']
    RPC_URL = context.bot_data['RPC_URL']
    
    wallet_manager = WalletManager(DATABASE_URL)
    user_manager = UserManager(DATABASE_URL)


    # Validate the wallet address
    if not wallet_manager.is_valid_solana_address(wallet_address):
        await update.message.reply_text("Invalid wallet address. Please try again.")
        return

    # Check if the wallet address exists
    if not wallet_manager.check_wallet_existence(wallet_address, RPC_URL):
        await update.message.reply_text("Wallet address does not exist. Please try again.")
        return

    # Get the user ID
    user_id = update.message.from_user.id
    user = user_manager.get_user_by_telegram_id(user_id)

    # Check if the user exists
    if not user:
        await update.message.reply_text("User not found. Please register first. run /start")
        return

    # Add the wallet address
    if wallet_manager.add_wallet(wallet_address):
        await update.message.reply_text(f"Wallet address {wallet_address} added successfully.")
    else:
        await update.message.reply_text("Wallet already added")
    
    # Link the wallet address to the user
    user_manager.add_wallet_to_user(user_id, wallet_address)