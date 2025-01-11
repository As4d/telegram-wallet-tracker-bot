from sqlalchemy import (
    Column, String, Integer, Float, ForeignKey, DateTime, JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Define models (e.g., User, Wallet, UserWallet, Transaction) here

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, unique=True, nullable=False)  # Unique Telegram user ID
    username = Column(String)  # Optional Telegram username
    preferences = Column(JSON, default={})  # JSON for notification preferences
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    # Define relationship with UserWallet
    wallets = relationship('UserWallet', back_populates='user')

class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, unique=True, nullable=False)  # Solana wallet address
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    # Define relationship with UserWallet
    users = relationship('UserWallet', back_populates='wallet')

class UserWallet(Base):
    __tablename__ = 'user_wallets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallets.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship('User', back_populates='wallets')
    wallet = relationship('Wallet', back_populates='users')
