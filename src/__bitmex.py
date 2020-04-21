import websocket
import threading
import time
from ast import literal_eval
import pprint

class BitmexReader (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data_list = []
        self.last_orderbook = []
        endpoint = 'wss://www.bitmex.com/realtime?subscribe=orderBook10:XBTUSD'
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(endpoint,
                                         on_open = self._on_open,
                                         on_message = self._on_message,
                                         on_error = self._on_error,
                                         on_close = self._on_close)

    def _on_open(self, ws):
        print("open")

    def _on_message(self, ws, message):
        if 'data' in message:
            message_dict = literal_eval(message)
            orderbook = message_dict['data'][0]
            if not self.last_orderbook:
                self.last_orderbook = orderbook
            else:
                self._compare_orderbook(orderbook, self.last_orderbook)
                self.last_orderbook = orderbook

    def _on_error(self, ws, error):
        self.ws._on_close(ws)

    def _on_close(self, ws):
        self.ws.close()

    def run(self):
        self.ws.run_forever()

    def _update(self, side, price, change):
        best = self.last_orderbook[side][0][0]
        self.data_list.append({'side':side, 'best':best, 'distance':abs(price-best), 'size':change})

    def _compare_orderbook(self, newbook, oldbook):
        for side in ['asks', 'bids']:
            new_it = 0
            old_it = 0
            while True:
                if new_it >= len(newbook[side]) or old_it >= len(oldbook[side]):
                    break
                new_price = newbook[side][new_it][0]
                old_price = oldbook[side][old_it][0]
                new_size = newbook[side][new_it][1]
                old_size = oldbook[side][old_it][1]
                if new_price == old_price:
                    if new_size != old_size:
                        self._update(side, new_price, new_size - old_size)
                        new_it += 1
                        old_it += 1
                    else:
                        new_it += 1
                        old_it += 1
                else:
                    if new_price > old_price:
                        if side is 'asks':
                            self._update(side, old_price, -old_size)
                            old_it += 1
                        else:
                            self._update(side, new_price, new_size)
                            new_it += 1
                    else:
                        if side is 'asks':
                            self._update(side, new_price, new_size)
                            new_it += 1
                        else:
                            self._update(side, old_price, -old_size)
                            old_it += 1


    def _sum_orderbook(self):
        total_buy = 0
        total_sell = 0
        if self.last_orderbook:
            for buy_order in self.last_orderbook['bids']:
                total_buy += buy_order[1]
            for sell_order in self.last_orderbook['asks']:
                total_sell += sell_order[1]

        return total_buy, total_sell

    def get_data(self):
        total_buy, total_sell = self._sum_orderbook()
        data = {'time':time.time(), 'total_buy': total_buy, 'total_sell': total_sell,
                'orders': self.data_list}
        self.data_list = []
        return data



br = BitmexReader()
br.start()
while True:
    time.sleep(1)
    pprint.pprint(br.get_data())
