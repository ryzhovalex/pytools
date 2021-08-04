import sys
from typing import Literal

from loguru import logger

from .singleton import Singleton


class Logger(metaclass=Singleton):
    """ 
    Logger model responsible of writing all actions to logs. 
    Simply said - it is a layer between program and loguru created for holding one loguru.logger through all program. 
    """
    def __init__(self, mode: Literal["prod", "dev"]) -> None:
        if mode == "prod":
            logger.add("main.log", format="{time} {level} {message}", level="INFO", serialize=True, compression="zip", rotation="10 MB")
        elif mode == "dev":
            logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", serialize=True, compression="zip", rotation="10 MB")

    @staticmethod
    def debug(message: str) -> None:
        logger.debug(message)

    @staticmethod
    def info(message: str) -> None:
        logger.info(message)

    @staticmethod
    def warning(message: str) -> None:
        logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        logger.error(message)
        
    @staticmethod
    def critical(message: str) -> None:
        logger.critical(message)
