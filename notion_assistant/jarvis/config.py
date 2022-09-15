from copy import deepcopy
from dataclasses import dataclass
from typing import List, Dict

from defaultenv import env


@dataclass
class JarvisPluginConfig:
    name: str
    enabled: bool

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


# Jarvis
@dataclass
class JarvisConfig:
    plugins: Dict[str, JarvisPluginConfig]
    notion_token: str
    db_logs: str
    db_structured_logs: str
    jarvis_env: str

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


jarvis_config = JarvisConfig(
    plugins=dict(),
    notion_token=env("JARVIS_NOTION_TOKEN"),
    db_logs=env("JARVIS_SIMPLE_LOG_TABLE"),
    db_structured_logs=env("JARVIS_STUCTURED_LOG_TABLE"),
    jarvis_env=env("JARVIS_ENV")  # prod or dev
)

# Jarvis Input Bot
plugin = JarvisPluginConfig(
    name='JarvisInputBot',
    enabled=True
)
plugin.telegram_token = env("JARVIS_TELEGRAM_INPUT_TOKEN")
plugin.db_todos = env("JARVIS_DB_TODOS")
plugin.db_notes = env("JARVIS_DB_NOTES")
plugin.db_bookmarks = env("JARVIS_DB_BOOKMARKS")
jarvis_config.plugins[plugin.name] = plugin

# Jarvis Output Bot
plugin = JarvisPluginConfig(
    name='JarvisOutputBot',
    enabled=True
)
plugin.telegram_token = env("JARVIS_TELEGRAM_TOKEN")
jarvis_config.plugins[plugin.name] = plugin

# Simple task Selector
plugins = JarvisPluginConfig(
    name='JarvisSimpleTaskSelectorBot',
    enabled=False
)
plugins.telegram_token = env("JARVIS_TELEGRAM_STS_TOKEN")
jarvis_config.plugins[plugin.name] = plugin

# Simple task repeater
plugin = JarvisPluginConfig(
    name='SimpleTaskRepeater',
    enabled=False
)
plugin.db_str = env("JARVIS_DB_STR")
jarvis_config.plugins[plugin.name] = plugin
