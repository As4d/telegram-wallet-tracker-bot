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
    
    def get_wallet_balance(self, address: str, rpc_url: str) -> float:
        """Fetches wallet balance from the Solana blockchain."""
        try:
            balance_payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getBalance",
                "params": [address]
            }
            balance_response = requests.post(rpc_url, json=balance_payload)
            balance_data = balance_response.json()
            balance = balance_data.get("result", {}).get("value", 0) / 1e9  # Convert lamports to SOL
            return balance
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to connect to the Solana RPC API: {e}")

    def get_wallet_tokens(self, address: str, rpc_url: str) -> list:
        """Fetches token holdings from the Solana blockchain."""
        try:
            token_payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getTokenAccountsByOwner",
                "params": [
                    address,
                    {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
                    {"encoding": "jsonParsed"}
                ]
            }
            token_response = requests.post(rpc_url, json=token_payload)
            token_data = token_response.json()

            tokens = []
            for token_account in token_data.get("result", {}).get("value", []):
                parsed_info = token_account.get("account", {}).get("data", {}).get("parsed", {}).get("info", {})
                mint = parsed_info.get("mint")
                token_amount_info = parsed_info.get("tokenAmount", {})
                amount = int(token_amount_info.get("amount", 0))
                decimals = int(token_amount_info.get("decimals", 0))
                tokens.append({
                    "mint": mint,
                    "amount": amount / (10 ** decimals)  # Convert amount based on token decimals
                })

            return tokens
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to connect to the Solana RPC API: {e}")
