"""
This module provides the WalletManager class for managing Solana wallet addresses 
and interacting with a data storage system and the Solana blockchain.
Classes:
    WalletManager: A class responsible for managing wallet addresses, validating them, 
    and checking their existence on the Solana blockchain.
Dependencies:
    base58: A module for base58 encoding and decoding.
    requests: A module for making HTTP requests.
    storage.data_storage: A module containing the DataStorage class for database operations.
"""

import base58
import requests
from storage.data_storage import DataStorage


class WalletManager:
    """
    WalletManager is a class responsible for managing wallet addresses 
    and interacting with a data storage system and the Solana blockchain.
    Attributes:
        data_storage (DataStorage): An instance of DataStorage to handle database operations.
    Methods:
        __init__(database_url: str):
            Initializes the WalletManager with a database URL.
        add_wallet(wallet_address: str) -> bool:
            Adds a wallet address to the database.
        is_valid_solana_address(address: str) -> bool:
            Validates if a Solana wallet address is base58 encoded and of correct length.
        check_wallet_existence(address: str, rpc_url: str) -> bool:
            Checks if a wallet address exists on the Solana blockchain.
    """

    def __init__(self, database_url: str):
        self.data_storage = DataStorage(database_url)

    def add_wallet(self, wallet_address: str) -> bool:
        """Adds a wallet address to the database."""
        try:
            self.data_storage.add_wallet(wallet_address)
            return True
        except ValueError:
            return False


    def is_valid_solana_address(self, address: str) -> bool:
        """Validates if a Solana wallet address is base58 encoded and of correct length."""
        if not address or len(address) != 44:
            return False
        try:
            # Attempt to decode the address using base58
            base58.b58decode(address)
            return True
        except ValueError:
            return False

    def check_wallet_existence(self, address: str, rpc_url: str) -> bool:
        """Checks if a wallet address exists on the Solana blockchain."""
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [address, {"encoding": "jsonParsed"}]
        }
        try:
            response = requests.post(rpc_url, json=payload, timeout=10)
            response_data = response.json()
            # If `value` is None, the wallet doesn't exist
            return response_data.get("result", {}).get("value") is not None
        except requests.RequestException as exc:
            raise ConnectionError("Failed to connect to the Solana RPC API.") from exc
