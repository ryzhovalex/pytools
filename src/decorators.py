""" Kit with various decorators. """
import requests


def catch_request_connection_error(function):
    def wrapper(*args, **kwargs):
        try:
            print("INFO: Sending request...")
            response = function(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            print(f"ERROR: Address not responding!")
        else:
            print(f"INFO: ...request has been sent with {response=}!")
        finally:
            return response
    return wrapper