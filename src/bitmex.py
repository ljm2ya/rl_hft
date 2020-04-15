import websocket
import threading
from time import sleep

class BitmexWebSocket (threading.Thread):
    '''
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

    def __init__(self, subscript, pair = 'XBTUSD'):
        threading.Thread.__init__(self)
        self.endpoint = 'wss://www.bitmex.com/realtime?subscribe='+subscript+':'+pair
        self.received_data = []
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.endpoint,
                                         on_open = self._on_open,
                                         on_message = self._on_message,
                                         on_error = self._on_error,
                                         on_close = self._on_close)

    def _on_message(self, ws, message):
        self.received_data.append(message)

    def _on_open(self, ws):
        print("websocket open")

    def _on_error(self, ws):
        print("error")
        self.ws._on_close(ws)

    def _on_close(self, ws):
        self.ws.close()

    def run(self):
        self.ws.run_forever()

'''
class BitmexOrder:
    def __init__(self, api_key, api_secret, pair = 'XBTUSD'):
'''