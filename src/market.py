import websocket
import threading
import json
import time
import os
from pprint import pprint

class BaseWebSocket (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def _init_websocket(self, endpoint):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(endpoint,
                                         on_open = self._on_open,
                                         on_message = self._on_message,
                                         on_error = self._on_error,
                                         on_close = self._on_close)

    def _on_open(self, ws):
        self._reset()

    def _on_message(self, ws, message):
        message = json.loads(message)
        self.data.append(message)

    def _on_error(self, ws, error):
        print(error)
        self._on_close(ws)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def _on_close(self, ws):
        self.ws.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def _reset(self):
        self.data = []

    def _check_data(self):
        return True if self.data else False

    def run(self):
        self.ws.run_forever()

    def get_data(self):
        if self._check_data():
            data = self.data
            self._reset()
            return data

class BinanceWebSocket (BaseWebSocket):
    def __init__(self, *streams):
        threading.Thread.__init__(self)
        #stream = "stream?streams=" + '/'.join(map(str, streams))
        stream = 'ws/btcusdt@forceOrder'
        endpoint = "wss://fstream.binance.com/"
        #stream = "stream?streams=btcusdt@aggTrade/btcusdt@forceOrder/btcusdt@bookTicker/btcusdt@depth@0ms"

class BitmexWebSocket (BaseWebSocket):
    def __init__(self, *subscriptions):
        self._reset()
        threading.Thread.__init__(self)
        subscription = ','.join(map(str, subscriptions))
        endpoint = 'wss://www.bitmex.com/realtime?subscribe='+subscription
        self._init_websocket(endpoint)


socket = BitmexWebSocket('orderBookL2_25:XBTUSD', 'trade:XBTUSD')
socket.start()
while True:
    time.sleep(1)
    print(socket.get_data())

'''
class BinanceLOBRecorder:
    def __init__(self, interval):
        self.ws = BinanceWebSocket('btcusdt@aggTrade', 'btcusdt@forceOrder', 'btcusdt@bookTicker', 'btcusdt@depth')
        self.lasttime = time.time()
        self.orderBook = {'A': [], 'B': []} # A: ask, B: bid
        self.aggTrade = {'B': [], 'S': []} # B: buy, S: sell
        self.aggLiquidation = {'A': [], 'B': []} # A: ask, B:bid
        self.fundingfee = {'F': 0, 'T': 0} # F: funding fee, T: time left until next fund

    def get_data(self):
        data =

    def __classify_stream(self, data):
        stream = data['stream']
        if stream == 'aggTrade':
            self.__update_aggTrade(data['data'])
        elif stream == 'forceOrder':
            self.__update


re = BinanceLOBRecorder()
re.start(1)
'''
