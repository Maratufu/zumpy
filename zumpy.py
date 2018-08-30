import os
from telegram.ext import Updater, CommandHandler
updater = Updater(token=os.environ['TOKEN'])


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater(tk)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
