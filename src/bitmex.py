import websocket
import threading
import json
import time

class BitmexWebSocket (threading.Thread):
    def __init__(self, *subscriptions):
        self.__reset()
        threading.Thread.__init__(self)
        self.subscription = subscriptions
        subscription = ':XBTUSD,'.join(map(str, subscriptions))
        endpoint = 'wss://www.bitmex.com/realtime?subscribe='+subscription+':'+pair
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
        print(error)
        self.__on_close(ws)

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
