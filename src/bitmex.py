#!/usr/bin/env python3
import websocket
import threading
from time import sleep
import sys
import json

class BitmexWebSocket (threading.Thread):
    '''
    BitMEX WebSocket Subscriptions
    "announcement",        // Site announcements
    "chat",                // Trollbox chat
    "connected",           // Statistics of connected users/bots
    "funding",             // Updates of swap funding rates. Sent every funding interval (usually 8hrs)
    "instrument",          // Instrument updates including turnover and bid/ask
    "insurance",           // Daily Insurance Fund updates
    "liquidation",         // Liquidation orders as they're entered into the book
    "orderBookL2_25",      // Top 25 levels of level 2 order book
    "orderBookL2",         // Full level 2 order book
    "orderBook10",         // Top 10 levels using traditional full book push
    "publicNotifications", // System-wide notifications (used for short-lived messages)
    "quote",               // Top level of the book
    "quoteBin1m",          // 1-minute quote bins
    "quoteBin5m",          // 5-minute quote bins
    "quoteBin1h",          // 1-hour quote bins
    "quoteBin1d",          // 1-day quote bins
    "settlement",          // Settlements
    "trade",               // Live trades
    "tradeBin1m",          // 1-minute trade bins
    "tradeBin5m",          // 5-minute trade bins
    "tradeBin1h",          // 1-hour trade bins
    "tradeBin1d",          // 1-day trade bins
    '''
    def __init__(self, *subscriptions):
        self.__reset()
        pair = 'XBTUSD'
        self.subscription = subscriptions
        subscription = ':XBTUSD,'.join(map(str, subscriptions))
        endpoint = 'wss://www.bitmex.com/realtime?subscribe='+subscription+':'+pair
        threading.Thread.__init__(self)
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(endpoint,
                                         on_open = self.__on_open,
                                         on_message = self.__on_message,
                                         on_error = self.__on_error,
                                         on_close = self.__on_close)

    def __on_open(self, ws):
        self.__reset()

    def __on_message(self, ws, message):
        message = json.loads(message)
        if 'data' in message:
            table = message['table']
            self.data[table] = message['data']

    def __on_error(self, ws, error):
        f = open('error.txt', 'w')
        stdout = sys.stdout
        sys.stdout = f
        print(error)
        f.close()

        #self.data['error'] = error
        raise websocket.WebSocketException(error)
        sleep(1)
        self.__init__(self.subscription)
        self.start()

    def __on_close(self, ws):
        self.ws.close()

    def __reset(self):
        self.data = {}

    def check_data(self):
        return True if self.data else False

    def run(self):
        self.ws.run_forever()

    def get_data(self):
        data = self.data
        self.__reset()
        return data
