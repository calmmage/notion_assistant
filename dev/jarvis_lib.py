"""
Temporary file for misc
"""
import notion_client
from telegram.ext import Updater

# abstract telegram
class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(self.token)

    @property
    def dispatcher(self):
        return self.updater.dispatcher

    def start(self):
        self.updater.start_polling()

# todo: parse commands decorator - pull from Alex branch
# todo: example function with usage


# Jarvis-specific telegram


# Abstract Notion

# Jarvis-specific Notion

# utils

# 1) connect Notion
# 2) connect Telegram
# 3) Do something - add task handler


# 2) connect Telegram
import telegram.ext
telegram_updater = telegram.ext.Updater(env("JARVIS_TELEGRAM_TOKEN"))

# 3) add message handler

class NotionClient:
    def __init__(self, token):
        self.client = notion_client.Client(auth=token)

    # var1 - message text, tags - tags.
    def add_task(self, name, content, tags):
        """
        Example:
        /add_task New task to cleanup #home sdf #urgent sdf

        [] Clean up kitchen etc #idea
        [] clean up desk
        #2hours

        :param text:
        :param tags:
        :return:
        """
        pars = {"parent": {"database_id": TASKS_DB_ID},
                "properties": {
                    "Name": {
                        "title": [
                            {
                                "text": {
                                    "content": name,
                                },
                            },
                        ],
                    },
                },
                }
        if content:
            pars["children"] = [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content,
                                },
                            },
                        ],
                    },
                },
            ]
        self.client.pages.create(**pars)


def parse_command(full_command):
    """
    Parse telegram command format for Jarvis

    Examples:
    1. Simple command example:
    >>> parse_command('/idea Test jarvis #link Notion Assistant #blue #important')
    {'command': '/idea', 'text': 'Test jarvis', 'tags': {'link': 'Notion Assistant', 'blue': None, 'important': None}}

    2. Text only
    >>> parse_command('Just text with tags #link Notion Assistant #blue #important')
    {'command': None, 'text': 'Just text with tags', 'tags': {'link': 'Notion Assistant', 'blue': None, 'important': None}}
    """
    output = {}

    # parse command
    if full_command.startswith('/'):
        command, message = full_command.split(None, 1)
        output['command'] = command.rstrip()
    else:
        message = full_command
        output['command'] = None

    text, *tags = message.split('#')

    # parse text
    text = text.strip()
    if '\n' in text.strip():
        # text with content, for example in
        # /idea Make tests
        # So that everything is tested
        # #Important
        text, content = text.split('\n', 1)
        output['name'] = text
        output['content'] = content
    else:
        output['name'] = text
        output['content'] = None

    # parse tags
    tags = [[part.rstrip() for part in tag.split(None, 1)] for tag in tags]
    output['tags'] = dict([(tag + [None] if len(tag) == 1 else tag) for tag in tags])

    return output

# %%
def notion_decorator(func):
    def new_func(upd, cont):
        parts = parse_command(upd.message.text)
        res = func(name=parts['name'], content=parts['content'], tags=parts['tags'])
        if res:
            upd.message.reply_text(res)

    return new_func