import logging

NOTSET = logging.NOTSET
INFO = logging.INFO
DEBUG = logging.DEBUG
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

LOG_FORMAT = '%(asctime)s.%(msecs)03d | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'


def set_logging(log_level: int = logging.INFO):
    logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATEFMT, level=log_level)
