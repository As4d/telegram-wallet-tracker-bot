from telegram import Update
from telegram.ext import ContextTypes
from ..wallet_manager import WalletManager


async def list_wallet_tokens_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles fetching tokens for a wallet when the inline button is clicked."""
    query = update.callback_query
    await query.answer()  # Acknowledge the callback to avoid timeout

    _, wallet_address = query.data.split(":")  # Extract wallet address from callback data
    RPC_URL = context.bot_data['RPC_URL']

    try:
        wallet_manager = WalletManager(context.bot_data['DATABASE_URL'])
        tokens = wallet_manager.get_wallet_tokens(wallet_address, RPC_URL)

        if not tokens:
            await query.edit_message_text(f"No tokens found for wallet: `{wallet_address}`", parse_mode="Markdown")
            return

        token_list = "\n".join([
            f"- Mint: `{token['mint']}`\n  Amount: {round(token['amount'], 3)} 🪙"
            for token in tokens if token['amount'] > 0
        ])
        message = f"**Tokens for Wallet:** `{wallet_address}`\n\n{token_list}"
        await query.edit_message_text(message, parse_mode="Markdown")
    except ConnectionError as e:
        await query.edit_message_text(f"Error: {str(e)}")
    except Exception as e:
        await query.edit_message_text("An unexpected error occurred (Probably too many tokens). Please try again later.")
