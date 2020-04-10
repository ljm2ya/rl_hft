#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt
from market import Binance
from calculator import calc_DOBI


plt.figure()
client = Binance('BTCUSDT')

while 10:
    old_obook = client.get_orderbook(100)
    time.sleep(1)
    new_obook = client.get_orderbook(100)
    trades = client.get_recent_trades(100)
    print(calc_DOBI(new_obook, old_obook, trades))
    print("midprice:")
    print(new_obook['asks'][0][0])
