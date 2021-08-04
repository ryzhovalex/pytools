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
        self.logger = logger
        if not Logger.init_flag: # call function below only once at first initialization to avoid TypeError (calling Logger without arguments)
            self.logger.add(*args, **kwargs)

        # initialize class function variables
        Logger.debug = self.logger.debug
        Logger.info = self.logger.info
        Logger.warning = self.logger.warning
        Logger.error = self.logger.error
        Logger.critical = self.logger.critical
    
    @property
    def logger(self):
        return self.logger
    
