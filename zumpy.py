from botinfo import token
from telegram.ext import Updater, CommandHandler
updater = Updater(token=token)

dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='\
     Olá, fui ligado! :) ')

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)


updater.start_polling()
