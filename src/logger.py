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

    ## These variables will contain appropriate logging functions after class's initialization for convenient external usage ##
    debug = None
    info = None
    warning = None
    error = None
    critical = None

    # 'True' if instance has initialized before
    init_flag = False

    def __init__(self, *args, **kwargs) -> None:
        self.native_logger = logger
        if not Logger.init_flag: # call function below only once at first initialization to avoid TypeError (calling Logger without arguments)
            self.log.add(*args, **kwargs)

        # initialize class function variables
        Logger.debug = self.native_logger.debug
        Logger.info = self.native_logger.info
        Logger.warning = self.native_logger.warning
        Logger.error = self.native_logger.error
        Logger.critical = self.native_logger.critical
    
    def get_native_logger(self):
        return self.native_logger
    
