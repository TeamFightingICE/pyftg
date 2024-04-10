import logging

INFO = logging.INFO
DEBUG = logging.DEBUG
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


def set_logging(log_level: int = logging.INFO):
    logging.basicConfig(format='%(asctime)s.%(msecs)03d | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=log_level)
