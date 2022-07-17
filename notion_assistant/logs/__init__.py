import logging

from .setup_logging import setup_logger

logging.basicConfig(level=logging.INFO)

LOGGER = setup_logger()
