#!/usr/bin/env python3
from binance.client import Client

class Binance:
    def __init__(self, symbol):#symbol is BTCUSDT
        self.client = Client()
        self.symbol = symbol

    def get_orderbook(self, count):
        return self.client.futures_order_book(symbol=self.symbol, limit=count)

    def get_recent_trades(self, count):
        return self.client.futures_recent_trades(symbol=self.symbol, limit=count)
