import os
import pickle

class Reader:
    def __init__(self, data_dir, initial_date):
        self.target_dir = data_dir + '/' + str(initial_date)
        self.walk = self.__walk_files(self.target_dir)

    def __walk_files(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                yield file

    def __next_dir(self, last_dir):
        parent_dir = os.path.dirname(last_dir)
        dir_list = os.listdir(parent_dir)
        last_dir_name = last_dir.split(os.path.sep).pop()
        last_dir_index = dir_list.index(last_dir_name)

        return parent_dir + dir_list[last_dir_index+1]

    def next_file(self):
        try:
            return next(self.walk)
        except:
            try:
                self.target_dir = self.__next_dir(self.target_dir)
                self.walk = self.__walk_files(self.target_dir)
                self.next_file()
            except:
                return 'last file'

reader = Reader(os.getcwd()+'/data', 1)
while True:
    n = reader.next_file()
    if n is not 'last file':
        print(n)
    else:
        print(n)
        break
