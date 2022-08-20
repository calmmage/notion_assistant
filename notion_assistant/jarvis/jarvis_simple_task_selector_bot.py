from notion_assistant.jarvis.config import jarvis_simple_task_selector_bot_config
from notion_assistant.jarvis.telegram_client import TelegramClient
from notion_assistant.logs import LOGGER


class JarvisSimpleTaskSelectorBot:
    def __init__(self, jarvis):
        self.jarvis = jarvis
        self.notion_client = jarvis.notion_client

        self.telegram_client = TelegramClient(jarvis_simple_task_selector_bot_config.telegram_token)

    def run(self):
        LOGGER.info(f"Launching {self.__class__.__name__}")
        # register telegram handlers
        # todo: find notebook - http://localhost:8888/notebooks/notion_assistant/dev/Simple%20task%20selector.ipynb
        # - start: do what is necessary to init: 1) fix notion db. check it's valid 2) select first task
        # commands:
        # - done
        # - skip
        # - blocked
        # - cleanup - get a db view to manually adjust statuses/priorities.

        # todo: auto-cleanup old messages / clutter

        # launch telegram bot
        self.telegram_client.run(blocking=False)

# Jarvis.registered_plugins.append(JarvisSimpleTaskSelectorBot)
