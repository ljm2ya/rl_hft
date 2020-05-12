import configparser
import threading

from reader import Reader
from agent import DRQN


class
class Trainer:
    def __init__(self, pretrained_nn = None):
        self.reader = Reader(data_dir, initial_date)
        self.agent = DRQN()
        self._load_hyperparameters()


    def _load_hyperparameters(self):
        config = configparser.ConfigParser()
        config.read('config.ini')


    def __get_environments(self, data):
        return environments

    def start(self, episode):
