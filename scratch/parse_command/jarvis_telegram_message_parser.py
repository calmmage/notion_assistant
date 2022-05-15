import functools
from telegram import Update

def telegram_command_to_text(func):
    @functools.wraps(func)
    def _get_text_and_apply(update: Update):
        return func(update.message.text)

    return _get_text_and_apply
