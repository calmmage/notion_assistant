"""
Temporary file for misc
"""

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
