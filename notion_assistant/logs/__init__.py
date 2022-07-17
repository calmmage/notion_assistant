import json
import logging

from .setup_logging import setup_logger

logging.basicConfig(level=logging.NOTSET)

with open('secrets.json') as secrets_file:
    secrets = json.load(secrets_file)

LOGGER = setup_logger(secrets)
