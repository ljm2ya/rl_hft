import os
import pickle

class Reader:
    def __init__(self, data_dir, initial_date):
        self.target_dir = data_dir + '/' + initial_date

    def __walk_files(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                yield file

    def __next_day(self, last_dir):
        parent_dir = os.path.dirname(last_dir)
        dir_list = os.listdir(parent_dir)
        last_dir_name = last_dir.split(os.path.sep).pop()
        last_dir_index = dir_list.index(last_dir_name)

        return parent_dir + dir_list[last_dir_index+1]

    #미완성
    def next_file(self):
        try:
            return next(self.__walk_files(self.target_dir))
        except:
            try:
                self.target_dir = self.__next_day(self.target_dir)
            except:
                return 'last file'
