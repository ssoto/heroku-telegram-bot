#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          InlineQueryHandler, )

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = '585421530:AAEvq5r9Imkeuhcr95axCauIfENu_oMdkyU'

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

greeting_message = ''' Hola soy el bot del proyecto Som Aigua

Ahora mismo estoy programado para:
* Procesar enlaces

Para ello necesitas darte de alta como usuaria. Escribe a Sergio Soto para poder
empezar a colaborar con nosotras.
'''

def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=greeting_message)
start_handler = CommandHandler('start', start)
logging.info('Added start handler')
dispatcher.add_handler(start_handler)

def info_text(bot, update):
    message = update.message.text

    reply = '''
    > {}
    El texto ha sido guardado'''.format(message)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply
    )

info_handler = CommandHandler('info', info_text)
dispatcher.add_handler(info_handler)
logging.info('Added info handler')


def unknown(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Perdona, pero no tengo configurado ese comando",
    )

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
logging.info('Added unknown handler')


updater.start_polling()
