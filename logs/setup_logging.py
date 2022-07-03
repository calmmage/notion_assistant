import logging
from handlers import get_all_log_handlers


def setup_logger() -> logging.Logger:
    """https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial"""

    handlers = get_all_log_handlers()
    for handler in handlers:
        logging.getLogger('').addHandler(handler) # TODO: adding directly to root loggger may be unsafe?
