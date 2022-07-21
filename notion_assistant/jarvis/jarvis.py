from time import sleep

from notion_assistant.jarvis.config import jarvis_config
from notion_assistant.jarvis.enhanced_notion_client import EnhancedNotionClient
from notion_assistant.logs import LOGGER


class JarvisPlugin:
    pass


class Jarvis:
    registered_plugins = []

    def __init__(self):
        # connect to Notion
        self.notion_client = EnhancedNotionClient(jarvis_config.notion_token)
        self.launched = False

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


if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.run()
