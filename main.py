"""
This script initializes and runs a Telegram bot using asyncio. It loads environment variables,
sets up signal handlers for graceful shutdown, and starts the bot.
Modules:
    asyncio: Provides support for asynchronous programming.
    bot.telegram_bot: Contains the TelegramBot class for bot operations.
    os: Provides a way of using operating system dependent functionality.
    dotenv: Loads environment variables from a .env file.
    signal: Provides mechanisms to use signal handlers in Python.
Functions:
    main(): The main entry point for the script. Loads environment variables, initializes the bot,
            sets up signal handlers, and runs the bot.
Usage:
    Run this script directly to start the Telegram bot.
"""

import asyncio
import os
import signal
from dotenv import load_dotenv
from bot.telegram_bot import TelegramBot

async def main():
    """The main entry point for the script."""
    load_dotenv()
    bot_token = os.getenv("bot_token")
    database_url = os.getenv("database_url")
    rpc_url = os.getenv("rpc_url")

    if not bot_token:
        raise ValueError("bot_token not found in environment variables")

    if not database_url:
        raise ValueError("database_url not found in environment variables")

    bot = TelegramBot(token=bot_token, database_url=database_url, rpc_url=rpc_url)

    def signal_handler(_, __):
        """Handle shutdown signals"""
        print("\nShutdown signal received. Cleaning up...")
        bot.stop_signal.set()  # This will trigger the bot to stop

    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)    # Handles Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)   # Handles termination signal

    try:
        await bot.run()
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    finally:
        print("Cleanup complete")

if __name__ == "__main__":
    if os.name == 'nt':  # Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
