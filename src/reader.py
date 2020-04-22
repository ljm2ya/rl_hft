import os
import pickle

class Reader:
    def __init__(self, data_dir, initial_date):
        self.initial_dir = data_dir + '/' + initial_date

    def __next_dir(self, last_dir):
        last_dir_name = last_dir.split(os.path.sep).pop()
        last_dir_index = dir_list.index(last_dir_name)
        parent_dir = os.path.dirname(last_dir)
        dir_list = os.listdir(parent_dir)

        if last_dir_index < len(dir_list)-1:
            return parent_dir + dir_list[last_dir_index+1]
        else:
            return self.__next_dir(parent_dir)
