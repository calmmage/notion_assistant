from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


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


class TelegramClient:
    def __init__(self, token):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher

        self.add_command_handler('start', start)
        self.add_command_handler('help', help_command)
        self.add_message_handler(Filters.text & ~Filters.command, echo)

    def add_command_handler(self, command, func):
        handler = CommandHandler(command, func)
        self.dispatcher.add_handler(handler)

    def add_message_handler(self, filters, func):
        handler = MessageHandler(filters, func)
        self.dispatcher.add_handler(handler)

    def run(self, blocking: bool):
        # Start the Bot
        print("Starting bot with token:", self.updater.bot.token)
        self.updater.start_polling()

        if blocking:
            self.updater.idle()
