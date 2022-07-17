import functools

from telegram import Update
from telegram.ext import CallbackContext

from .jarvis_command_parser import parse_command


def telegram_command_to_text(func):
    @functools.wraps(func)
    def _get_text_and_apply(update: Update):
        return func(update.message.text)

    return _get_text_and_apply


def notion_decorator(func):
    @functools.wraps(func)
    def new_func(upd: Update, context: CallbackContext) -> None:
        parts = parse_command(upd.message.text)
        res = func(parts['text'], parts['tags'])
        if res:
            upd.message.reply_text(res)
    return new_func

