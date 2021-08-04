import sys
from typing import Callable, Literal

from loguru import logger

from .singleton import Singleton


class Logger(metaclass=Singleton):
    """ 
    Logger tool responsible of writing all actions to logs. 
    Simply said - it is a layer between program and loguru created for holding one loguru.logger through all program. 
    """
    def __init__(self, *args, **kwargs) -> None:
        logger.add(*args, **kwargs)

    def get(self) -> logger:
        return logger

    @staticmethod
    def debug() -> Callable:
        return logger.debug

    @staticmethod
    def info() -> Callable:
        return logger.info

    @staticmethod
    def warning() -> Callable:
        return logger.warning

    @staticmethod
    def error() -> Callable:
        return logger.error

    @staticmethod
    def critical() -> Callable:
        return logger.info


## Twin functions of Logger for external direct importing ##
def debug() -> Callable:
    return Logger.debug

def info() -> Callable:
    return Logger.info

def warning() -> Callable:
    return Logger.warning

def error() -> Callable:
    return Logger.error

def critical() -> Callable:
    return Logger.info


