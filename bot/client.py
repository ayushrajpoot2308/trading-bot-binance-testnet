import os
from binance.client import Client

def get_client():
    return Client(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET"),
        testnet=True
    )