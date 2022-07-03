import logging
from handlers import get_all_log_handlers


def setup_logger() -> logging.Logger:
    """https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial"""
    logger = logging.getLogger(__name__)

    handlers = get_all_log_handlers()
    for handler in handlers:
        logger.addHandler(handler)

    logging.root = logger # TODO: may be unsafe?
