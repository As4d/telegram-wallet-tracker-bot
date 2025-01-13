from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from bot.commands.start_command import start_command
from bot.commands.help_command import help_command
from bot.commands.add_wallet_command import add_wallet_command
import logging
import asyncio

class TelegramBot:
    def __init__(self, token: str, database_url: str, rpc_url: str):
        if not token:
            raise ValueError("Bot token cannot be empty")
            
        self.token = token
        self.database_url = database_url
        self.rpc_url = rpc_url
        try:
            self.app = Application.builder().token(self.token).build()
            self.app.bot_data['DATABASE_URL'] = self.database_url
            self.app.bot_data['RPC_URL'] = self.rpc_url
        except Exception as e:
            raise RuntimeError(f"Failed to initialize bot: {str(e)}")

        # Setup logging
        logging.basicConfig(
            format='%(asctime)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def setup_handlers(self):
        self.app.add_handler(CommandHandler("start", start_command))
        self.app.add_handler(CommandHandler("help", help_command))
        self.app.add_handler(CommandHandler("add", add_wallet_command))

    async def run(self):
        try:
            self.setup_handlers()
            self.logger.info("Bot is starting...")
            await self.app.initialize()
            await self.app.start()
            await self.app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
            
            # Create a never-ending event to keep the bot running
            self.stop_signal = asyncio.Event()
            await self.stop_signal.wait()
            
        except Exception as e:
            self.logger.error(f"Error running bot: {str(e)}")
            raise
        finally:
            self.logger.info("Shutting down...")
            # First stop polling for updates
            await self.app.updater.stop()
            # Then stop the application
            await self.app.stop()
            # Finally, clean up
            await self.app.shutdown()
