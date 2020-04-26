#!/usr/bin/env python3
from reader import Reader

class Backtester:
    def __init__(self, data_dir, initial_date):
        self.reader = Reader(data_dir, initial_date)



    def __next_episode(self):
        data = self.reader.next_file()
        environments = self.__get_environments(data)




    def __get_environments(self, data):
        return environments
