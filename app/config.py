# config.py
import os
from getpass import getpass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for Flask app."""
    
    # General settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

    # Database settings
    DB_USER = os.getenv('DB_USER', 'default_user')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'default_db')

    # DB_PASSWORD will be set once when prompted
    DB_PASSWORD = None

    @classmethod
    def get_db_password(cls):
        """Get the database password (prompt if not in environment)."""
        if cls.DB_PASSWORD is None:
            cls.DB_PASSWORD = os.getenv('DB_PASSWORD') or getpass("Enter database password: ")
        return cls.DB_PASSWORD

    @classmethod
    def get_database_uri(cls):
        """Construct the database URI with the password."""
        db_password = cls.get_db_password()  # Ensure password is retrieved only once
        return f"postgresql://{cls.DB_USER}:{db_password}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
