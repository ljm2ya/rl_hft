#!/usr/bin/env python3

import pickle
import time
from bitmex import BitmexWebSocket

class BitmexRecorder:
    def __init__(self):
        self.socket = BitmexWebSocket('orderBook10', 'trade')

    def start_recording(self, interval, target):
        self.socket.start()

    def _
