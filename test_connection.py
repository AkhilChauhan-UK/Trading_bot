from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

print("Testing keys:", api_key[:6], api_secret[:6])

client = Client(api_key, api_secret)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

try:
    result = client.futures_account()
    print("✅ SUCCESS: Account info loaded!")
except Exception as e:
    print("❌ ERROR:", e)
