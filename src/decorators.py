""" Kit with various decorators. """
import requests
from .logger import Logger as log


@log.catch
def catch_request_connection_error(function):
    def wrapper(*args, **kwargs):
        response = None
        try:
            log.info("Sending request...")
            response = function(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            log.warning(f"Post request address is not responding!")
        else:
            log.info(f"Request has been sent with {response=}!")
        finally:
            return response
    return wrapper