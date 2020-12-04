import logging
from functools import wraps
import os


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ROOT_DIR = os.path.abspath(os.curdir)
        log_file = os.path.join(ROOT_DIR, 'tensorfree.log')
        log_form = "[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"

        logging.basicConfig(
            level=logging.DEBUG, format=log_form, filename=log_file, filemode='w+'
        )

        logger = logging.getLogger('wrap_logger')
        logger.debug(f'{func.__name__}')

        return func(*args, **kwargs)

    return wrapper

