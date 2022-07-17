import logging

from defaultenv import env
from .handlers import get_all_log_handlers


def setup_logger(logger_name="jarvis-logger") -> logging.Logger:
    """https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial"""

    logger = logging.getLogger(logger_name)

    handlers = get_all_log_handlers(notion_database_id=env("JARVIS_DB_LOGS"),
                                    notion_secret_key=env("JARVIS_NOTION_TOKEN"))
    for handler in handlers:
        logger.addHandler(handler)  # TODO: adding directly to root loggger may be unsafe?

    return logger
