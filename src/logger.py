import sys
from typing import Callable, Literal, Type

from loguru import logger

from .singleton import Singleton


class Logger(metaclass=Singleton):
    """ 
    Logger tool responsible of writing all actions to logs. 
    Simply said - it is a layer between program and loguru created for holding one loguru.logger through all program. 

    Usage:
    from path.to.logger import Logger
    Logger(*your_args, **your_kwargs)
    Logger.debug("hello!")
    """

    native_logger = logger  # loguru.logger itself

    ## initialize class function variables
    debug = native_logger.debug
    info = native_logger.info
    warning = native_logger.warning
    error = native_logger.error
    critical = native_logger.critical

    def __init__(self, *args, **kwargs) -> None:
        Logger.create_logger(*args, **kwargs)

    @classmethod
    def create_logger(cls, *args, **kwargs) -> int:
        return cls.native_logger.add(*args, **kwargs)

    @classmethod
    def remove_logger(cls, id: int) -> None:
        cls.native_logger.remove(id)

    @classmethod
    def get_native_logger(cls):
        return cls.native_logger

    @classmethod
    def catch(cls, func):
        return cls.native_logger.catch(func)
    
    
