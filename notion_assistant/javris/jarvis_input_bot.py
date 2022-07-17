# example: /task, /idea
# example: search. e.g. apps: /diary /daily plan etc.
# auto-cleanup old messages

import config
from jarvis import Jarvis
from notion_assistant.javris.telegram_client import TelegramClient


class JarvisInputBot:
    def __init__(self, jarvis):
        # init config values: telegram token etc.

        self.jarvis = jarvis
        self.notion_client = jarvis.notion_client

        # init telegram client
        self.telegram_client = TelegramClient(config.telegram_input_token)

    def run(self):
        # register telegram handlers
        # - /task
        # - /idea
        # ----
        # - /diary, daily diary
        # - /plan, daily plan

        # todo: auto-cleanup old messages / clutter

        # launch telegram bot
        self.telegram_client.run(blocking=False)


Jarvis.registered_plugins.append(JarvisInputBot)
