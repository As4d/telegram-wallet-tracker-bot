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

    def validate_user_id(self, user_id: str) -> bool:
        # Add validation logic for user ID
        return True if user_id else False