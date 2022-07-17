from .setup_logging import setup_logger

import json 
import logging

logging.basicConfig(level=logging.NOTSET)

with open('secrets.json') as secrets_file:
    secrets  = json.load(secrets_file)

LOGGER = setup_logger(secrets)
