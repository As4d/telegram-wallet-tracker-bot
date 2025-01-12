from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes
from ..wallet_manager import WalletManager
import os

DATABASE_URL = os.getenv("DATABASE_URL")

async def add_wallet_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /add command."""
    wallet_address = context.args[0] if context.args else None
    if not wallet_address:
        await update.message.reply_text("Please provide a wallet address.")
        return

    wallet_manager = WalletManager(DATABASE_URL)
    if wallet_manager.add_wallet(wallet_address):
        await update.message.reply_text(f"Wallet address {wallet_address} added successfully.")
    else:
        await update.message.reply_text("Invalid wallet address or already exists. Please try again.")