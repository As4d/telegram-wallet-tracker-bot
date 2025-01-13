"""
Module for initializing the database.

This module provides a function `init_db` that initializes the database by
creating all tables defined in the metadata. It uses SQLAlchemy to connect
to the database specified in the environment variable `DATABASE_URL`.
"""

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from .models import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    """
    Initializes the database by creating all tables defined in the metadata.
    This function creates a new SQLAlchemy engine using the DATABASE_URL and
    then creates all tables defined in the Base metadata. It prints a success
    message upon completion.
    Returns:
        None
    """
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
