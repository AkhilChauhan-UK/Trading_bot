import os
import logging
from config import API_KEY, API_SECRET
from binance.client import Client
from basic_bot import BasicBot
from utils import validate_symbol, validate_quantity, validate_price
from binance.enums import *


# ✅ Ensure log directory exists
os.makedirs("log", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename='log/bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

bot = BasicBot(API_KEY, API_SECRET)

print("=== Simplified Binance Futures Bot ===")

symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
while not validate_symbol(symbol):
    symbol = input("Invalid symbol. Try again (e.g., BTCUSDT): ").upper()

side = input("Enter order side (BUY/SELL): ").upper()
while side not in ["BUY", "SELL"]:
    side = input("Invalid. Enter BUY or SELL: ").upper()
side = SIDE_BUY if side == "BUY" else SIDE_SELL

order_type = input("Order type (MARKET/LIMIT): ").upper()
while order_type not in ["MARKET", "LIMIT"]:
    order_type = input("Invalid. Enter MARKET or LIMIT: ").upper()
order_type = ORDER_TYPE_MARKET if order_type == "MARKET" else ORDER_TYPE_LIMIT

quantity = input("Enter quantity: ")
while not validate_quantity(quantity):
    quantity = input("Invalid quantity. Try again: ")
quantity = float(quantity)

price = None
if order_type == ORDER_TYPE_LIMIT:
    price = input("Enter limit price: ")
    while not validate_price(price):
        price = input("Invalid price. Try again: ")
    price = float(price)

# Place the order
response = bot.place_order(symbol, side, order_type, quantity, price)
print("Order Response:", response)

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://testnet.binancefuture.com'
print("Loaded key:", API_KEY[:5], "secret:", API_SECRET[:5])
# Ensure the bot is connected to Binance Futures