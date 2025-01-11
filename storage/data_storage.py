from sqlalchemy.orm import Session
from storage.models import User, Wallet, UserWallet, Base
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from datetime import datetime

class DataStorage:
    """Handles database operations for the Wallet Tracker Bot."""

    def __init__(self, database_url: str):
        """Initializes the DataStorage instance.

        Args:
            database_url (str): URL of the database (e.g., SQLite, PostgreSQL).
        """
        self.engine = create_engine(database_url)
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)

    def add_user(self, telegram_id: str, username: str = None, preferences: dict = None) -> User:
        """Adds a new user to the database.

        Args:
            telegram_id (str): Telegram user ID.
            username (str, optional): Telegram username. Defaults to None.
            preferences (dict, optional): Notification preferences. Defaults to {}.

        Returns:
            User: The newly created User object.
        """
        try:
            new_user = User(
                telegram_id=telegram_id,
                username=username,
                preferences=preferences or {},
                created_at=datetime.utcnow(),
            )
            self.session.add(new_user)
            self.session.commit()
            return new_user
        except IntegrityError:
            self.session.rollback()
            raise ValueError(f"User with telegram_id {telegram_id} already exists.")

    def get_user(self, telegram_id: str) -> User:
        """Fetches a user by their Telegram ID.

        Args:
            telegram_id (str): Telegram user ID.

        Returns:
            User: The User object, or None if not found.
        """
        return self.session.query(User).filter(User.telegram_id == telegram_id).first()

    def add_wallet(self, address: str) -> Wallet:
        """Adds a new wallet to the database.

        Args:
            address (str): Solana wallet address.

        Returns:
            Wallet: The newly created Wallet object.
        """
        try:
            new_wallet = Wallet(address=address, created_at=datetime.utcnow())
            self.session.add(new_wallet)
            self.session.commit()
            return new_wallet
        except IntegrityError:
            self.session.rollback()
            raise ValueError(f"Wallet with address {address} already exists.")

    def get_wallet(self, address: str) -> Wallet:
        """Fetches a wallet by its address.

        Args:
            address (str): Solana wallet address.

        Returns:
            Wallet: The Wallet object, or None if not found.
        """
        return self.session.query(Wallet).filter(Wallet.address == address).first()

    def link_user_wallet(self, telegram_id: str, wallet_address: str) -> UserWallet:
        """Links a user to a wallet in the database.

        Args:
            telegram_id (str): Telegram user ID.
            wallet_address (str): Solana wallet address.

        Returns:
            UserWallet: The UserWallet object representing the association.
        """
        user = self.get_user(telegram_id)
        wallet = self.get_wallet(wallet_address)
        if not user or not wallet:
            raise ValueError("User or Wallet not found.")
        user_wallet = UserWallet(user_id=user.id, wallet_id=wallet.id, created_at=datetime.utcnow())
        self.session.add(user_wallet)
        self.session.commit()
        return user_wallet

    def get_user_wallets(self, telegram_id: str) -> list:
        """Fetches all wallets linked to a user.

        Args:
            telegram_id (str): Telegram user ID.

        Returns:
            list: A list of Wallet objects.
        """
        user = self.get_user(telegram_id)
        if not user:
            raise ValueError("User not found.")
        return (
            self.session.query(Wallet)
            .join(UserWallet, Wallet.id == UserWallet.wallet_id)
            .filter(UserWallet.user_id == user.id)
            .all()
        )

    def close(self):
        """Closes the database session."""
        self.session.close()
