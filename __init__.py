import json 

from logs import setup_logger
import scratch.NA_mvp

with open('secrets.json') as secrets_file:
    secrets  = json.load(secrets_file)

setup_logger(secrets)
