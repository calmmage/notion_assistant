from time import sleep

from notion_assistant.jarvis.config import jarvis_config
from notion_assistant.jarvis.enhanced_notion_client import EnhancedNotionClient
from notion_assistant.logs import LOGGER

import threading

import json
from copy import deepcopy
from pathlib import Path
# class JarvisPlugin:
#     pass

registered_users_path = Path("./registered_jarvis_users.json")

class Jarvis:
    registered_plugins = []

    def __init__(self, **kwargs):
        self.config = deepcopy(jarvis_config)
        self.config.__dict__.update(**kwargs)  # todo: figure out a better way to update config / turn on and off the plugins
        # connect to Notion
        self.notion_client = EnhancedNotionClient(jarvis_config.notion_token)
        self.launched = False

        if registered_users_path.exists():
            registered_users = json.load(registered_users_path.open('r'))
        else:
            registered_users = {}  # Dict[str,str]: User -> ChatId
        self.registered_users = registered_users

    def run(self):
        LOGGER.info(f"Launching {self.__class__.__name__}")
        # for Plugin in self.registered_plugins:

        from notion_assistant.jarvis.jarvis_input_bot import JarvisInputBot
        from notion_assistant.jarvis.jarvis_output_bot import JarvisOutputBot
        from notion_assistant.jarvis.jarvis_simple_task_selector_bot import \
            JarvisSimpleTaskSelectorBot

        plugin_registry = {
            "JarvisInputBot": JarvisInputBot,
            "JarvisOutputBot": JarvisOutputBot,
            "JarvisSimpleTaskSelectorBot": JarvisSimpleTaskSelectorBot,
            # c.__name__: c for c in JarvisPlugin.__subclasses__()
        }
        for plugin_config in jarvis_config.plugins:
            if not plugin_config.enabled:
                continue
            plugin = plugin_registry[plugin_config.name](self)
            plugin.run()

        self.launched = True
        while self.launched:
            sleep(1)

    def run_async(self):
        t = threading.Thread(target=self.run)
        t.run()
        return t


if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.run()
