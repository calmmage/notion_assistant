import logging

from .handlers import get_all_log_handlers


def setup_logger(secrets) -> logging.Logger:
    """https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial"""

    logger = logging.getLogger(secrets['loggername'])

    handlers = get_all_log_handlers(secrets['notion_log_db_id'], secrets['notion_token'])
    for handler in handlers:
        logger.addHandler(handler) # TODO: adding directly to root loggger may be unsafe?

    return logger
