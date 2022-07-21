from time import sleep

from notion_assistant.jarvis import config
from notion_assistant.jarvis.enhanced_notion_client import EnhancedNotionClient
from notion_assistant.logs import LOGGER


class Jarvis:
    registered_plugins = []

    def __init__(self):
        # connect to Notion
        self.notion_client = EnhancedNotionClient(config.notion_token)
        self.launched = False

    def run(self):
        LOGGER.info(f"Launching {self.__class__.__name__}")
        for Plugin in self.registered_plugins:
            plugin = Plugin(self)
            plugin.run()

        self.launched = True
        while self.launched:
            sleep(1)


if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.run()
