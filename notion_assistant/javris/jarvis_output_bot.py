# jarvis output bot

import config
from jarvis import Jarvis
# example: links for quick access relevant at this time of day (e.g. Siri)
# auto-cleanup all other clutter messages
from notion_assistant.javris.telegram_client import TelegramClient


# example: daily agenda.


class JarvisOutputBot:
    def __init__(self, jarvis):
        # init config values: telegram token etc.

        self.jarvis = jarvis
        self.notion_client = jarvis.notion_client

        self.telegram_client = TelegramClient(config.telegram_sts_token)

    def run(self):
        # register telegram handlers
        # - none for now. ? Or do 'diary' and other app lookup here instead of input?

        # background processes
        # - daily agenda
        # - recommended apps

        # todo: auto-cleanup old messages / clutter

        # launch telegram bot
        self.telegram_client.run(blocking=False)


Jarvis.registered_plugins.append(JarvisOutputBot)
