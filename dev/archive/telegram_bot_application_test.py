#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.
from defaultenv import env

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import telegram.ext

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


class TelegramClient:
    def __init__(self, token):
        self.updater = telegram.ext.Updater(token)
        self.dispatcher = self.updater.dispatcher

    def add_command_handler(self, command, func):
        handler = CommandHandler(command, func)
        self.dispatcher.add_handler(handler)

    def add_message_handler(self, filters, func):
        handler = MessageHandler(filters, func)
        self.dispatcher.add_handler(handler)

    def run(self, blocking: bool):
        # Start the Bot
        self.updater.start_polling()

        if blocking:
            # Run the bot until you press Ctrl-C or the process receives SIGINT,
            # SIGTERM or SIGABRT. This should be used most of the time, since
            # start_polling() is non-blocking and will stop the bot gracefully.
            self.updater.idle()


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher


if __name__ == "__main__":
    token = env("JARVIS_TELEGRAM_STS_TOKEN")
    t1 = TelegramClient(token)
    t1.add_command_handler('start', start)
    t1.add_command_handler('help', help_command)
    t1.add_message_handler(Filters.text & ~Filters.command, echo)

    t1.run(False)

    token = env("JARVIS_TELEGRAM_TOKEN")
    t2 = TelegramClient(token)
    t2.add_command_handler('start', start)
    t2.add_command_handler('help', help_command)
    t2.add_message_handler(Filters.text & ~Filters.command, echo)
    t2.run(False)

    token = env("JARVIS_TELEGRAM_INPUT_TOKEN")
    t3 = TelegramClient(token)
    t3.add_command_handler('start', start)
    t3.add_command_handler('help', help_command)
    t3.add_message_handler(Filters.text & ~Filters.command, echo)
    t3.run(False)

    t1.updater.idle()
