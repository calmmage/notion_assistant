from logging import StreamHandler, FileHandler
import logging

from notion_client import Client


class NotionLoggingHandler(StreamHandler):
    def __init__(self, notion_database_id, notion_secret_key):
        super().__init__()
        self.notion_client = Client(auth=notion_secret_key)
        self.notion_database_id = notion_database_id
        

    def emit(self, record: logging.LogRecord):
        if 'logging_parsing_result' in record.args:
            self._log_parsing_result(record)
        else:
            self._log_ordinary_result(record)


    def _log_parsing_result(self, record: logging.LogRecord):
        self.notion_client.pages.create(
            parent={"database_id": self.notion_database_id},
            properties=NotionLoggingHandler._parse_message_to_page(record),
            children=[
                {
                    "object": 'block',
                    "type": 'paragraph',
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": 'text',
                                "text": {
                                    "content": record.args['logging_parsing_result'],
                                },
                            },
                        ],
                    },
                },
            ]
        )

    def _log_ordinary_result(self, record: logging.LogRecord):
        self.notion_client.pages.create(
            parent={"database_id": self.notion_database_id},
            properties=NotionLoggingHandler._parse_message_to_page(record)
        )

    @staticmethod
    def _parse_message_to_page(record: logging.LogRecord):
        return {
                "level": {
                    "select": {
                        "name": record.levelname,
                    }
                },
                "message": {
                    "title": [
                        {
                            "text": {
                                "content": record.getMessage(),
                            },
                        },
                    ],
                },
            }

def get_all_log_handlers(
        notion_database_id,
        notion_secret_key,
        strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        logfile_path = 'logs.txt',
):
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    file_handler = FileHandler(logfile_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    notion_handler = NotionLoggingHandler(notion_database_id, notion_secret_key)
    notion_handler.setLevel(logging.DEBUG)
    notion_handler.setFormatter(formatter)

    handlers = [
        stream_handler,
        file_handler,
        notion_handler
    ]

    return handlers
