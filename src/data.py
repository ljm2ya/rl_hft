#!/usr/bin/env python3

from bitmex import BitmexWebSocket

class DataRefiner:
    def __init__(self):
        self.ts = BitmexWebSocket('trade')
        self.os = BitmexWebSocket('orderBook10')

    def run(self):
        self.ts.start()
        self.os.start()
