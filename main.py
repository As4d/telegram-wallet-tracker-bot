import asyncio
from bot.telegram_bot import TelegramBot
import os
from dotenv import load_dotenv
import signal



async def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    RPC_URL = os.getenv("RPC_URL")

    if not BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")
    
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not found in environment variables")
    
    bot = TelegramBot(token=BOT_TOKEN, database_url=DATABASE_URL, rpc_url=RPC_URL)
    
    def signal_handler(sig, frame):
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
