from dotenv import load_dotenv
import os
import secrets

load_dotenv()  # Load .env variables

class Config:
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    secret_key = secrets.token_hex(16)
    SECRET_KEY = os.environ.get('SECRET_KEY', secret_key)
