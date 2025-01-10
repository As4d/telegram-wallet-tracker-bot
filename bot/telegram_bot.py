from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from bot.commands import start_command, help_command
import logging
import asyncio

class TelegramBot:
    def __init__(self, token: str):
        if not token:
            raise ValueError("Bot token cannot be empty")
            
        self.token = token
        try:
            self.app = Application.builder().token(self.token).build()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize bot: {str(e)}")

        # Setup logging
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def setup_handlers(self):
        # Register the /start command
        self.app.add_handler(CommandHandler("start", start_command))
        self.app.add_handler(CommandHandler("help", help_command))

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
