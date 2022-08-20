# jarvis output bot
from typing import List

from notion_assistant.jarvis import config
from notion_assistant.jarvis.jarvis import Jarvis
# example: links for quick access relevant at this time of day (e.g. Siri)
# auto-cleanup all other clutter messages
from notion_assistant.jarvis.telegram_client import TelegramClient
# example: daily agenda.
from notion_assistant.jarvis.temp import parse_telegram_command_decorator
from notion_assistant.logs import LOGGER


def telegram_command(commands: List[str]):
    if isinstance(commands, str):
        commands = [commands]

    def wrapper(func):
        # add func to registry
        for command in commands:
            telegram_command.registry[command] = func.__name__
        return func

    return wrapper


telegram_command.registry = dict()


class JarvisOutputBot:
    commands = dict()

    def __init__(self, jarvis):
        # init config values: telegram token etc.

        self.jarvis = jarvis
        self.notion_client = jarvis.notion_client

        self.telegram_client = TelegramClient(config.telegram_sts_token)

    @telegram_command(['daily_diary', 'diary'])
    def get_daily_diary(self):
        # todo: replace hardcode with config sourced from notion table
        return "https://www.notion.so/lavrovs/Daily-Diary-f13e3e2a11014da7b8d875d71b9d6b20"

    @telegram_command(['daily_plans', 'plans', 'schedule'])
    def get_daily_plans(self):
        # todo: replace hardcode with config sourced from notion table
        return "https://www.notion.so/lavrovs/Daily-Plans-fbb2c8966f1c47ebb257eb2b34ba30c2"

    def run(self):
        pligin_name = self.__class__.__name__
        LOGGER.info(f"Launching {pligin_name}")
        # register telegram handlers
        # - none for now. ? Or do 'diary' and other app lookup here instead of input?

        # background processes
        # - daily agenda
        # - recommended apps

        # todo: auto-cleanup old messages / clutter

        for command, func_name in telegram_command.registry.items():
            func = self.__getattribute__(func_name)
            func = parse_telegram_command_decorator(
                func)
            self.telegram_client.add_handler(command, func)
            LOGGER.info(f"Added handler <{func}> for command <{command}>  in plugin {pligin_name}")

        # launch telegram bot
        self.telegram_client.run(blocking=False)
        LOGGER.info(f"Plugin {pligin_name} is running")


Jarvis.registered_plugins.append(JarvisOutputBot)
