#!/usr/bin/env python3
import json
from bitmex import BitmexDataRefiner
#from binance import BinanceDataRefiner


class DataRecorder:
    def __init__(self, market):
        if market is 'bitmex':
            self.dr = BitmexDataRefiner()
        elif market is 'binance':
            self.dr = BinanceDataRefiner()
        else:
            print("error, no market named "+market)

    def run(self):
        self.dr.start()

dr = DataRefiner()
dr.run()
