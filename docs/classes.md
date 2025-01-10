# Core Classes Overview

## TelegramBot
- Handles integration with the Telegram API.
- Manages commands like `/start`, `/help`, `/add`, `/remove`, and `/list`.
- Maintains user interactions and provides responses.

## WalletManager
- Handles wallet-related operations such as adding, removing, and listing tracked wallets.
- Validates wallet addresses before adding them.

## NotificationManager
- Manages notifications for incoming, outgoing, and large transactions.
- Handles user preferences for notifications and thresholds.

## TransactionParser
- Parses raw transaction data fetched from the Solana API.
- Extracts details like:
  - Transaction type (incoming/outgoing)
  - Amount of SOL or tokens transferred
  - Sender and receiver addresses
  - Timestamp and block number

## DataStorage
- Interacts with the database to store user subscriptions, tracked wallets, and preferences.
- Ensures unique mappings between users and wallets.

## ApiService
- Integrates with the Solana API to fetch transaction data.
- Handles API connectivity, WebSocket management (if applicable), and error handling.

## Scheduler
- Manages periodic polling or WebSocket updates for wallet activities.
- Optimizes intervals to reduce API usage and ensure real-time tracking.

## Logger
- Logs bot performance, user interactions, and API requests.
- Helps with debugging and monitoring.
