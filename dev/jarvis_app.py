from defaultenv import env
# usage:
# env("JARVIS_NOTION_TOKEN")
# env("JARVIS_TELEGRAM_TOKEN")
from scratch.NA_mvp import extract_database_id
import notion_client as notion
import logging

TASKS_DATABASE = 'https://www.notion.so/lavrovs/d96416324b44433a9d378f0767627301?v=877e567e513a4583b9e4614d1b059ba1'
TASKS_DB_ID = extract_database_id(TASKS_DATABASE)


# from pathlib import Path
# # todo: create user-agnostic path or use resources
# # todo: get secrets from env
# secrets_path = Path('/Users/calm/home/notion_assistant/scratch/telegram_bot_example/secrets.json')
# import json
# secrets = json.load(secrets_path.open())

def jarvis_app():
    # 1) connect Notion
    # 2) connect Telegram
    # 3) Do something - add task handler

    # 1) connect Notion
    logging.info('Creating notion client...')
    notion_client = notion.Client(auth=env("JARVIS_NOTION_TOKEN"))
    logging.info('Created notion client')

    # 2) connect Telegram
    import telegram.ext
    logging.info('Creating telegram client...')
    telegram_updater = telegram.ext.Updater(env("JARVIS_TELEGRAM_TOKEN"))
    logging.info('Created telegram client')

    # 3) add message handler

    class NotionClient:
        def __init__(self, token):
            self.client = notion.Client(auth=token)

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
            logging.info('Starting telegram client...')
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

    # %%
    # 4) launch
    logging.info('Launching notion client...')
    nc = NotionClient(token=env("JARVIS_NOTION_TOKEN"))
    logging.info('Launched notion client...')

    dispatcher = telegram_updater.dispatcher
    dispatcher.add_handler(telegram.ext.CommandHandler("add_task",
                                                       notion_decorator(nc.add_task)))
    logging.info('Added telegram task handler...')

    # Start the Bot
    logging.info('Telegram bot is starting...')
    telegram_updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    logging.info('Telegram bot started')
    telegram_updater.idle()


if __name__ == '__main__':
    # Launch
    jarvis_app()
