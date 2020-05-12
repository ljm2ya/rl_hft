import os
import pickle
import time
import threading
from market import BitmexWebSocket

'''
class BitmexRecorder:
    def __init__(self, interval, target_dir):
        self.socket = BitmexWebSocket('orderBook10', 'trade')
        self.interval = interval
        self.target_dir = target_dir+'/data'
        if not os.path.isdir(self.target_dir):
            os.mkdir(self.target_dir)

    def start_recording(self):
        self.socket.start()
        self.__record()

    def __check_directory(self, today, minute):
        target_dir = self.target_dir+'/'+today+'/'+minute
        if not os.path.isdir(self.target_dir+'/'+today):
            os.mkdir(self.target_dir+'/'+today)
            os.mkdir(target_dir)
        else:
            os.mkdir(target_dir) if not os.path.isdir(target_dir) else None

        return target_dir

    def __record(self):
        if self.socket.check_data():
            bulk_data = self.socket.get_data()

            today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            minute = time.strftime('%H:%M', time.localtime(time.time()))
            target_dir = self.__check_directory(today, minute)
            target = target_dir + '/' + str(time.time())

            if 'trade' in bulk_data:
                data = {'orderbook': bulk_data['orderBook10'].pop(), 'trades':bulk_data['trade']}
            else:
                data = {'orderbook': bulk_data['orderBook10'].pop()}

            with open(target, 'wb') as f:
                pickle.dump(data, f)

        threading.Timer(self.interval, self.__record).start()

if __name__ == "__main__":
    recorder = BitmexRecorder(1, os.getcwd())
    recorder.start_recording()

'''


#ws = BitmexWebSocket('''liquidation', 'orderBookL2', 'trade')
ws = BitmexWebSocket('connected')
ws.start()
while True:
    time.sleep(1)
    print(ws.get_data())

