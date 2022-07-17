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
    from jarvis_lib import NotionClient, notion_decorator, telegram_updater
    import telegram.ext
    # %%
    # 4) launch
    notion_client = NotionClient(token=env("JARVIS_NOTION_TOKEN"))

    dispatcher = telegram_updater.dispatcher
    dispatcher.add_handler(telegram.ext.CommandHandler("add_task",
                                                       notion_decorator(notion_client.add_task)))

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
