from storage.data_storage import DataStorage

class WalletManager:
    def __init__(self, database_url: str):
        self.data_storage = DataStorage(database_url)

    def add_wallet(self, wallet_address: str) -> bool:
        if not self.validate_wallet_address(wallet_address):
            return False
        try:
            self.data_storage.add_wallet(wallet_address)
            return True
        except ValueError:
            return False

    def validate_wallet_address(self, wallet_address: str) -> bool:
        # Add validation logic for wallet address
        return True if wallet_address else False