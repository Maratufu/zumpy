import os
from telegram.ext import Updater, CommandHandler
updater = Updater(token=os.environ['TOKEN'])


def hello(bot, update):
    update.message.reply_text(
        'Olá {}, no momento estou em manuntenção!'.format(update.message.from_user.first_name))


updater.dispatcher.add_handler(CommandHandler('hello', hello))


updater.start_polling()
updater.idle()
