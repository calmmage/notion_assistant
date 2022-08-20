from dataclasses import dataclass
from typing import List

from defaultenv import env


@dataclass
class JarvisPluginConfig:
    name: str
    enabled: bool


# Jarvis
@dataclass
class JarvisConfig:
    plugins: List[JarvisPluginConfig]
    notion_token: str
    db_logs: str
    db_structured_logs: str
    jarvis_env: str


jarvis_config = JarvisConfig(
    plugins=[],
    notion_token=env("JARVIS_NOTION_TOKEN"),
    db_logs=env("JARVIS_SIMPLE_LOG_TABLE"),
    db_structured_logs=env("JARVIS_STUCTURED_LOG_TABLE"),
    jarvis_env=env("JARVIS_ENV")  # prod or dev
)

# Jarvis Input Bot
jarvis_input_bot_config = JarvisPluginConfig(
    name='JarvisInputBot',
    enabled=True
)
jarvis_input_bot_config.telegram_token = env("JARVIS_TELEGRAM_INPUT_TOKEN")
jarvis_input_bot_config.db_todos = env("JARVIS_DB_TODOS")
jarvis_input_bot_config.db_notes = env("JARVIS_DB_NOTES")
jarvis_input_bot_config.db_bookmarks = env("JARVIS_DB_BOOKMARKS")

jarvis_config.plugins.append(jarvis_input_bot_config)

# Jarvis Output Bot
jarvis_output_bot_config = JarvisPluginConfig(
    name='JarvisOutputBot',
    enabled=True
)
jarvis_output_bot_config.telegram_token = env("JARVIS_TELEGRAM_TOKEN")

jarvis_config.plugins.append(jarvis_output_bot_config)

# Simple task Selector
jarvis_simple_task_selector_bot_config = JarvisPluginConfig(
    name='JarvisSimpleTaskSelectorBot',
    enabled=False
)
jarvis_simple_task_selector_bot_config.telegram_token = env("JARVIS_TELEGRAM_STS_TOKEN")

jarvis_config.plugins.append(jarvis_simple_task_selector_bot_config)

# Simple task repeater
jarvis_simple_task_repeater_bot_config = JarvisPluginConfig(
    name='JarvisInputBot',
    enabled=False
)
jarvis_simple_task_repeater_bot_config.db_str = env("JARVIS_DB_STR")

jarvis_config.plugins.append(jarvis_simple_task_repeater_bot_config)
