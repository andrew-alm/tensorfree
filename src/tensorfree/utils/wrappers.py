import logging
from functools import wraps


def pred_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_form = "%(asctime)s - %(args)s"
        logging.basicConfig(
            level=logging.DEBUG, format=log_form, filename="predictions.log"
        )
        return func(*args, **kwargs)

    return wrapper
