from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

        logging.info("Bot initialized using testnet: %s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == ORDER_TYPE_MARKET:
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == ORDER_TYPE_LIMIT:
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            logging.info("Order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Order failed: %s", str(e))
            return {"error": str(e)}
