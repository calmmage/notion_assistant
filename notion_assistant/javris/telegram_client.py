import telegram.ext


class TelegramClient:
    def __init__(self, token):
        #         self.token = token
        self.updater = telegram.ext.Updater(token)
        self.dispatcher = self.updater.dispatcher

    def add_handler(self, command, func):
        handler = telegram.ext.CommandHandler(command, func)
        self.dispatcher.add_handler(handler)

    def run(self, blocking: bool):
        # Start the Bot
        self.updater.start_polling()

        if blocking:
            # Run the bot until you press Ctrl-C or the process receives SIGINT,
            # SIGTERM or SIGABRT. This should be used most of the time, since
            # start_polling() is non-blocking and will stop the bot gracefully.
            self.updater.idle()
