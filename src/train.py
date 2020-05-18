import os
import configparser
import threading

from data import BitmexData
from simulator import MarketSimulator

data = BitmexData()

envi


class Trainer:
    def __init__(self, pretrained_nn = None):
        self.agent = DRQN()
        self._load_hyperparameters()


    def _load_hyperparameters(self):
        config = configparser.ConfigParser()
        config.read('config.ini')


    def _get_environments(self, data):
        return environments

    def start(self, episode):
