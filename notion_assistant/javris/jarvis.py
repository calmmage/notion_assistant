# jarvis.py
from time import sleep

import config
from notion_assistant.javris.notion_client import NotionClient


class Jarvis:
    registered_plugins = []

    def __init__(self):
        # connect to Notion
        self.notion_client = NotionClient(config.notion_token)
        self.launched = False

    def run(self):
        for Plugin in self.registered_plugins:
            plugin = Plugin(self)
            plugin.run()

        self.launched = True
        while self.launched:
            sleep(1)


if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.run()
