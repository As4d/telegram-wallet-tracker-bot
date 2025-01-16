from storage.data_storage import DataStorage

class UserManager:
    def __init__(self, database_url: str):
        self.data_storage = DataStorage(database_url)

    def add_user(self, user_id: str, user_data: dict) -> bool:
        if not self.validate_user_id(user_id):
            return False
        try:
            self.data_storage.add_user(user_id, user_data)
            return True
        except ValueError:
            return False
    
    def user_exists(self, user_id: str) -> bool:
        return self.data_storage.get_user(user_id) is not None
    
    def get_user_by_telegram_id(self, telegram_id: str) -> dict:
        return self.data_storage.get_user(telegram_id)

    def add_wallet_to_user(self, user_id: str, wallet_address: str) -> bool:
        self.data_storage.link_user_wallet(user_id, wallet_address)

    def validate_user_id(self, user_id: str) -> bool:
        # Add validation logic for user ID
        return True if user_id else False

    def get_wallets_by_user_id(self, user_id: str) -> list:
        return self.data_storage.get_user_wallets(user_id)