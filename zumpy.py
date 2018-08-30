import os
import logging
from telegram.ext import Updater, CommandHandler
updater = Updater(token=os.environ['TOKEN.'])


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater.dispatcher.add_handler(CommandHandler('hello', hello))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\
 - %(message)s',  level=logging.INFO)

updater.start_polling()
updater.idle()
