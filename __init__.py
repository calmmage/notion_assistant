import json 
import logging

from logs import setup_logger
import scratch.NA_mvp

logging.basicConfig(level=logging.NOTSET)

with open('secrets.json') as secrets_file:
    secrets  = json.load(secrets_file)

LOGGER = setup_logger(secrets)
