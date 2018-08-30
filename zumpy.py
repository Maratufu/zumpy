import os
from telegram.ext import Updater, CommandHandler
updater = Updater(token=os.environ['TOKEN'])


def hello(bot, update):
    update.message.reply_text(
        'Hello {0} {1}'.format(update.message.from_user.first_name, os.environ['TOKEN']))


updater.dispatcher.add_handler(CommandHandler('hello', hello))


updater.start_polling()
updater.idle()
