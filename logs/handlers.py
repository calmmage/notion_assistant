from logging import StreamHandler, FileHandler
import logging

def get_all_log_handlers(
        strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        logfile_path = 'logs.txt'
):
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    file_handler = FileHandler(logfile_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    handlers = [
        stream_handler,
        file_handler
    ]

    return handlers
