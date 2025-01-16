from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from ..user_manager import UserManager
from ..wallet_manager import WalletManager

async def list_wallets_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /list command."""
    DATABASE_URL = context.bot_data['DATABASE_URL']
    RPC_URL = context.bot_data['RPC_URL']
    user_manager = UserManager(DATABASE_URL)
    wallet_manager = WalletManager(DATABASE_URL)
    
    user_id = update.message.from_user.id
    user = user_manager.get_user_by_telegram_id(user_id)
    
    if not user:
        await update.message.reply_text("User not found. Please register first. Run /start.")
        return
    
    wallets = user_manager.get_wallets_by_user_id(user_id)
    if not wallets:
        await update.message.reply_text("No wallets found. Please add a wallet first.")
        return
    
    wallet_list = [
    f"{i+1}. `{wallet.address}` - {round(wallet_manager.get_wallet_balance(wallet.address, RPC_URL), 3)} SOL 🪙"
    for i, wallet in enumerate(wallets)
]

    wallet_buttons = [
        [
            InlineKeyboardButton(
                text=f"View {wallet.address[0:5]}...'s Tokens",
                callback_data=f"tokens:{wallet.address}"
            )
        ]
        for wallet in wallets
    ]

    message = f"**Your Wallets:**\n" + "\n".join(wallet_list)

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(wallet_buttons)
    )

