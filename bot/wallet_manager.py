from storage.data_storage import DataStorage
import base58
import requests

class WalletManager:
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
            decoded = base58.b58decode(address)
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
            response = requests.post(rpc_url, json=payload)
            response_data = response.json()
            # If `value` is None, the wallet doesn't exist
            return response_data.get("result", {}).get("value") is not None
        except requests.RequestException:
            raise ConnectionError("Failed to connect to the Solana RPC API.")