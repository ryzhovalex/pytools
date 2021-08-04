import sys
from typing import Literal

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

