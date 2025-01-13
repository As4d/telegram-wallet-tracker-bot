"""
This module provides the UserManager class for managing user data 
and interacting with a data storage system.
Classes:
    UserManager: A class responsible for managing user data
    and interacting with a data storage system.
Dependencies:
    storage.data_storage: A module containing the DataStorage class for database operations.
"""

from storage.data_storage import DataStorage


class UserManager:
    """
    UserManager is a class responsible for managing user data 
    and interacting with a data storage system.
    Attributes:
        data_storage (DataStorage): An instance of DataStorage to handle database operations.
    Methods:
        __init__(database_url: str):
            Initializes the UserManager with a database URL.
        add_user(user_id: str, user_data: dict) -> bool:
            Adds a user to the database.
        user_exists(user_id: str) -> bool:
            Checks if a user exists in the database.
        get_user_by_telegram_id(telegram_id: str) -> dict:
            Retrieves user data by Telegram ID.
        add_wallet_to_user(user_id: str, wallet_address: str) -> bool:
            Links a wallet address to a user.
        validate_user_id(user_id: str) -> bool:
            Validates a user ID.
    """
    def __init__(self, database_url: str):
        """Initializes the UserManager with a database URL."""
        self.data_storage = DataStorage(database_url)

    def add_user(self, user_id: str, user_data: dict) -> bool:
        """Adds a user to the database."""
        if not self.validate_user_id(user_id):
            return False
        try:
            self.data_storage.add_user(user_id, user_data)
            return True
        except ValueError:
            return False

    def user_exists(self, user_id: str) -> bool:
        """Checks if a user exists in the database."""
        return self.data_storage.get_user(user_id) is not None

    def get_user_by_telegram_id(self, telegram_id: str) -> dict:
        """Retrieves user data by Telegram ID."""
        return self.data_storage.get_user(telegram_id)

    def add_wallet_to_user(self, user_id: str, wallet_address: str) -> bool:
        """Links a wallet address to a user."""
        self.data_storage.link_user_wallet(user_id, wallet_address)

    def validate_user_id(self, user_id: str) -> bool:
        """Validates a user ID."""
        # Add validation logic for user ID
        return True if user_id else False
