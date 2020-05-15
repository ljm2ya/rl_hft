import json

from reader import DataReader

class BitmexDataMiner:
    def __init__(self, data_dir, initial_date):
        self.reader = DataReader(data_dir, initial_date)


    def next_data(self):
        bulk_data = self.reader.next_file()

        return data


def bitmex_data_process(bulk_data):


    def _idtoprice(self, ID, symbolIdx=88, ticksize=0.01):
        price = ((100000000 * symbolIdx) - ID) * ticksize
        return price
