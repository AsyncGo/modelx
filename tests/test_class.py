import os
import sys

sys.path.append('../')
from config import config

class ClassTest:
    engines = {}

    def __init__(self):
        pass

    @staticmethod
    def initPool():
        print(config['dev'].DB_URI)

    @staticmethod
    def getSession():
        ClassTest.initPool()


if __name__ == '__main__':
    print(ClassTest.getSession())