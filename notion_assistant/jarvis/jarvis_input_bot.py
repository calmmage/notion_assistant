# example: /task, /idea
# example: search. e.g. apps: /diary /daily plan etc.
# auto-cleanup old messages

from typing import List, Optional

from notion_assistant.jarvis.enhanced_notion_client import NotionDB
from notion_assistant.jarvis.jarvis import Jarvis
from notion_assistant.jarvis.telegram_client import TelegramClient
from notion_assistant.jarvis.temp import parse_telegram_command_decorator, compose_item
from notion_assistant.logs import LOGGER
from notion_assistant.notion_db_enums.db_anchor_enums import C_Type


def generator(commands: List[str]):
    if isinstance(commands, str):
        commands = [commands]

    def wrapper(func):
        # add func to registry
        for command in commands:
            generator.registry[command] = func.__name__
        return func

    return wrapper


generator.registry = dict()


def tag_processor(tags: List[str]):
    if isinstance(tags, str):
        tags = [tags]

    def wrapper(func):
        # todo verify func signature: should accept item to apply tag to and query for the tag
        # add func to registry
        for tag in tags:
            tag_processor.registry[tag] = func.__name__
        return func

    return wrapper


tag_processor.registry = dict()


class JarvisInputBot:
    generator_commands = dict()
    tag_processors = dict()

    def __init__(self, jarvis: Jarvis):
        # init config values: telegram token etc.

        self.jarvis = jarvis
        jarvis_input_bot_config = jarvis.config.plugins['JarvisInputBot']
        self.notion_client = jarvis.notion_client

        self.db_todos = self.notion_client.get_db(jarvis_input_bot_config.db_todos)

        # init telegram client
        self.telegram_client = TelegramClient(jarvis_input_bot_config.telegram_token)

    @generator(commands=['add'])
    def add_item(self, name, tags, content=None, target_db: Optional[NotionDB] = None,
                 core_type: Optional[C_Type] = None):
        # compose item
        item = compose_item(name=name, content=content)
        for tag, query in tags.items():
            if tag not in tag_processor.registry:
                # raise RuntimeError(f"Unsupported tag: {tag}")
                LOGGER.warning(f"Unsupported tag: {tag}, content={content}")
                continue
            # check
            # todo: apply tags. Use tags processors
            processor = tag_processor.registry[tag]
            # todo: catch errors outside and add logging of errors
            item = processor(item=item, query=query)

        if target_db is None:
            # todo: mark page as unsorted - for future processing
            target_db = self.db_todos

        res = target_db.add_item(item)
        # todo: add logging
        # todo: use telegram formatted links instead of text links
        LOGGER.info(f'Page {name} of type {core_type} was added to DB {target_db} at {res}')
        return f"Page added successfully. Address: {res}"  # reply to the user.

    @generator(['todo', 'task'])
    def add_task(self, name, tags: dict, content=None):
        return self.add_item(name=name, tags=tags, content=content, target_db=self.db_todos,
                             core_type=C_Type.Todo)

    @generator(['idea'])
    def add_idea(self, name, tags: dict, content=None):
        return self.add_item(name=name, tags=tags, content=content, target_db=self.db_todos,
                             core_type=C_Type.Idea)

    # ----------------------
    # Tags

    @staticmethod
    def tag_metadata(item, value, column=None):
        """
        Add metadata to the Notion item json representation
        :param item: Notion nested json item to be modified
        :param value: field value to be added to the specified column
        :param column: column to add value to
        if column is None - add as generic tag.
        :return:
        """
        # todo: check possible values for specified column using notion db structure metadata. convert.
        # NotionDB.metadata
        raise NotImplemented()

    @tag_processor(['link', 'expose_to'])
    def tag_link(self, item, query):
        # todo: find page. what db? notion client

        # add metadata
        #
        raise NotImplemented("Linking is not implemented yet")

    @tag_processor(['who', 'source'])
    def tag_source(self, item, query):
        # find a person
        raise NotImplemented("Specifying source is not implemented yet")

    def run(self):
        pligin_name = self.__class__.__name__
        LOGGER.info(f"Launching {pligin_name}")
        # register telegram handlers
        # - /task
        # - /idea
        # ----
        # - /diary, daily diary
        # - /plan, daily plan

        for generator_command, func_name in generator.registry.items():
            func = self.__getattribute__(func_name)
            func = parse_telegram_command_decorator(func)
            self.telegram_client.add_command_handler(generator_command, func)
            LOGGER.info(f"Added handler <{func}> for command <{generator_command}> in plugin {pligin_name}")

        # todo p1: Add general text handler. Convert messages to commands and process accordingly

        # todo: auto-cleanup old messages / clutter

        # launch telegram bot
        self.telegram_client.run(blocking=False)
        LOGGER.info(f"Plugin {pligin_name} is running")

# Jarvis.registered_plugins.append(JarvisInputBot)
