import time
import threading

from reader import DataReader

class BackTester:
    def __init__(self, data_dir, start_day):
        self.reader = DataReader(data_dir, start_day)
        self.queuedOrders = []
        self.orderBook = {'buy':[], 'sell':[]}
        self.bestbuy
        self.bestsell

# model form
# model is class that has action selector, trainer(only ml model), report generator
# next() class method gets current env and generate propriate action return form is action
# get_report() class method returns model report

    def __check_order_sequence(self, side, price, sequence):

    #order form : order = {'num': 2, 'side': 'buy', 'price': 8394.3, 'quantity': 50, 'sequence': 3245}
    def check_order(self, order):
        if order['side'] == 'buy':
            if order['price'] > self.bestbuy:
                return 1
            elif order['price'] == self.bestbuy:
                return self.__check_order_sequence(order['side'], order['price'], order['sequence'])
            else:
                return 0
        else:
            if order['price'] < self.bestsell:
                return 1
            elif order['price'] == self.bestsell:
                return self.__check_order_sequence(order['side'], order['price'], order['sequence'])
            else:
                return 0

    def get_
# data form
# data = {'orderbook': [], 'trades': [], '}
    def next(self):
        data = self.reader.next_file()
        for model in models:

    def report(self):
