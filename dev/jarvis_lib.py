"""
Temporary file for misc
"""
from telegram.ext import Updater

import notion_client


# abstract telegram
class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(self.token)

    @property
    def dispatcher(self):
        return self.updater.dispatcher

    def start(self):
        self.updater.start_polling()

# todo: parse commands decorator - pull from Alex branch
# todo: example function with usage


# Jarvis-specific telegram


# Abstract Notion

# Jarvis-specific Notion

# utils

# 1) connect Notion
# 2) connect Telegram
# 3) Do something - add task handler


# 2) connect Telegram
import telegram.ext
telegram_updater = telegram.ext.Updater(env("JARVIS_TELEGRAM_TOKEN"))

# 3) add message handler

class NotionClient:
    def __init__(self, token):
        self.client = notion_client.Client(auth=token)

    # var1 - message text, tags - tags.
    def add_task(self, name, content, tags):
        """
        Example:
        /add_task New task to cleanup #home sdf #urgent sdf

        [] Clean up kitchen etc #idea
        [] clean up desk
        #2hours

        :param text:
        :param tags:
        :return:
        """
        pars = {"parent": {"database_id": TASKS_DB_ID},
                "properties": {
                    "Name": {
                        "title": [
                            {
                                "text": {
                                    "content": name,
                                },
                            },
                        ],
                    },
                },
                }
        if content:
            pars["children"] = [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content,
                                },
                            },
                        ],
                    },
                },
            ]
        self.client.pages.create(**pars)

# %%
