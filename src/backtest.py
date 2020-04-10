#!/usr/bin/env python3

import time
from market import Binance

class Backtest:
    def __init__(self, speed):
        self.speed = speed
