import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# ✅ Correct: Use the variable names in the .env file
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")
