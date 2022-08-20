import functools

from telegram import Update
from telegram.ext import CallbackContext

from notion_assistant.logs import LOGGER


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
    LOGGER.warning("Still using the old decommissioned parser!")
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
    output['tags'] = {
        tag[0]: (None if len(tag) == 1 else tag[1])
        for tag in tags
    }

    return output


def parse_telegram_command_decorator(func):
    # todo: add logging @akudrinskii
    @functools.wraps(func)
    def new_func(upd: Update, context: CallbackContext) -> None:
        parts = parse_command(upd.message.text)
        res = func(name=parts['name'], content=parts['content'], tags=parts['tags'])
        if res:
            upd.message.reply_text(res)

    return new_func


# supported generators registry: (Types of items that can be composed)
# todo: add. generic add
# todo: all the
def compose_block(content):
    return {
        "object": 'block',
        "type": 'paragraph',
        "paragraph": {
            "rich_text": [
                {
                    "type": 'text',
                    "text": {
                        "content": content,
                    },
                },
            ],
        },
    }


def compose_item(name, content=None):
    item = {'properties': ({
                               "Name": {
                                   "title": [
                                       {
                                           "text": {
                                               "content": name,
                                           },
                                       },
                                   ],
                               },
                           },)}
    if content:
        item['children'] = [compose_block(line) for line in content.split('\n')]
    return item
