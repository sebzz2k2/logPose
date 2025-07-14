from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()
class env(Enum):
    POSTGRES_DB = os.getenv("POSTGRES_DB", "default_db")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "default_user")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "default_password")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")