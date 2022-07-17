import logging

from .setup_logging import setup_logger

logging.basicConfig(level=logging.NOTSET)

LOGGER = setup_logger()
