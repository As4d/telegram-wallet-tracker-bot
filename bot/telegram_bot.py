"""
This module contains the implementation of a Telegram bot using the python-telegram-bot library.
The bot is designed to handle various commands such as start, help, and add wallet.
Classes:
    TelegramBot: A class that encapsulates the functionality of the Telegram bot.
Usage:
    To use this module, create an instance of the TelegramBot class with the required parameters
    and call the run method to start the bot.
Example:
    bot = TelegramBot(token="YOUR_BOT_TOKEN", database_url="YOUR_DATABASE_URL", 
    rpc_url="YOUR_RPC_URL")
    asyncio.run(bot.run())
"""

import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler
from bot.commands.start_command import start_command
from bot.commands.help_command import help_command
from bot.commands.add_wallet_command import add_wallet_command


class TelegramBot:
    """
    A class to represent a Telegram bot.
    Attributes:
    -----------
    token : str
        The token for the Telegram bot.
    database_url : str
        The URL for the database connection.
    rpc_url : str
        The URL for the RPC connection.
    stop_signal : asyncio.Event
        An asyncio event to signal the bot to stop.
    app : Application
        The application instance of the bot.
    logger : logging.Logger
        The logger instance for logging bot activities.
    Methods:
    --------
    __init__(token: str, database_url: str, rpc_url: str):
        Initializes the TelegramBot with the given token, database URL, and RPC URL.
    setup_handlers():
        Sets up the command handlers for the bot.
    run():
        Asynchronously runs the bot, setting up handlers, starting the bot, and handling shutdown.
    """

    def __init__(self, token: str, database_url: str, rpc_url: str):
        if not token:
            raise ValueError("Bot token cannot be empty")

        self.token = token
        self.database_url = database_url
        self.rpc_url = rpc_url
        self.stop_signal = asyncio.Event()
        try:
            self.app = Application.builder().token(self.token).build()
            self.app.bot_data['DATABASE_URL'] = self.database_url
            self.app.bot_data['RPC_URL'] = self.rpc_url
        except Exception as e:
            raise RuntimeError(f"Failed to initialize bot: {str(e)}") from e

        # Setup logging
        logging.basicConfig(
            format='%(asctime)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def setup_handlers(self):
        """
        Sets up the command handlers for the Telegram bot.
        This method adds handlers for the following commands:
        - /start: Triggers the start_command function.
        - /help: Triggers the help_command function.
        - /add: Triggers the add_wallet_command function.
        """

        self.app.add_handler(CommandHandler("start", start_command))
        self.app.add_handler(CommandHandler("help", help_command))
        self.app.add_handler(CommandHandler("add", add_wallet_command))

    async def run(self):
        """
        Runs the Telegram bot by initializing and starting the application, 
        setting up handlers, and starting polling for updates. Keeps the bot 
        running until a stop signal is received.
        This method handles exceptions that occur during the bot's execution 
        and ensures proper shutdown of the bot by stopping polling, stopping 
        the application, and performing cleanup.
        Raises:
            Exception: If an error occurs while running the bot.
        """

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
            self.logger.error("Error running bot: %s", str(e))
            raise
        finally:
            self.logger.info("Shutting down...")
            # First stop polling for updates
            await self.app.updater.stop()
            # Then stop the application
            await self.app.stop()
            # Finally, clean up
            await self.app.shutdown()
