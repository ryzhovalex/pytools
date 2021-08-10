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

    # loguru.logger itself
    native_logger = None

    ## These variables will contain appropriate logging functions after class's initialization for convenient external usage ##
    debug = None
    info = None
    warning = None
    error = None
    critical = None

    def __init__(self, *args, **kwargs) -> None:
        Logger.native_logger = logger
        Logger.create_logger(*args, **kwargs)

        # initialize class function variables
        Logger.debug = Logger.native_logger.debug
        Logger.info = Logger.native_logger.info
        Logger.warning = Logger.native_logger.warning
        Logger.error = Logger.native_logger.error
        Logger.critical = Logger.native_logger.critical

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
    
    
