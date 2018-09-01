'''
A maioria das informações estão no wiki/doc do python-telegram-bot `p-t-b`.
https://github.com/python-telegram-bot/python-telegram-bot/wiki

Resumo da introdução do p-t-b:

Classe          |     Significado

Updater         | Atualiza para o bot dados da conversa e passa os dados
                    para outra classe dispatcher.

Dispatcher      | Organiza os dados do updater e recebe um handle com
                    uma função definida no código.

CommandHandler  | Registra um handle atráves de um comando
                    no bot. ex: /hello


'''

import os
import logging
from telegram.ext import Updater, CommandHandler


'''
Opções para fazer DEBUG:

Caso queira ver o que o bot está recebendo de dados
só tirar o comentário dos logger.

'''
# Imprimi no console erros que não forem do tipo `TelegramError`
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\
- %(message)s', level=logging.INFO)

# Imprimi no console o DEBUG do bot
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

'''
TOKEN:

O token real do bot está guardado no servidor, por isso está sendo
usado com a biblioteca os.

Em desenvolvimento você pode testar seu código, com o token para o bot
de @ZumpyDevBot e assim conseguir acessar o console no seu
computador para ver os possiveis erros.

'''

# TOKEN do @ZumpyDevBot
# updater = Updater(token='546654873:AAGRrVzhicHqBzczWW2w9kGOm64LI6bezDM')

# TOKEN do @ZumpyBot
updater = Updater(token=os.environ['TOKEN'])

dispatcher = updater.dispatcher


def hello(bot, update):
    update.message.reply_text('Olá {} no momento estou em manuntenção!\
        '.format(update.message.from_user.first_name))


dispatcher.add_handler(CommandHandler('hello', hello))


updater.start_polling()
updater.idle()
