#Написать игру с конфетами через бота, вариант человек против человека

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd

bot = Bot(token='5739319837:AAH-lTFw2B22P54eBlDwLQLjX-fANwalxgU')
updater = Updater(token='5739319837:AAH-lTFw2B22P54eBlDwLQLjX-fANwalxgU')
dispatcher = updater.dispatcher

START = 0
FIRST = 1
SECOND = 2

def start(update, context):
    global flag
    global sweets 
    sweets = 2021
    first = rd(1, 2)
    print(first)
    flag = first
    context.bot.send_message(update.effective_chat.id, f'Давайте поиграем в конфеты. Всего их {sweets}\n'
                                                        'Берите не более 28 за раз. Выиграет тот,'
                                                        f'кто возьмет последним. Игрок {flag}, ходи первым: ')
    if flag == 1:
        return FIRST
    else:
        return SECOND

def first(update, context):
    global sweets 
    global flag
    print('first started') 
    sweets -= int(update.message.text)
    print('first', sweets)
    if sweets < 1:
        context.bot.send_message(update.effective_chat.id,f'Ура! Победил игрок {flag}')
        return ConversationHandler.END
    else:
        flag = 2
        context.bot.send_message(update.effective_chat.id, f'Осталось {sweets} конфет.\n Теперь'
                                                                f'ходит игрок {flag}')
        print('first flag==2')
        return SECOND

def second(update, context):
    global sweets 
    global flag
    print('second started')
    sweets -= int(update.message.text)
    print('second', sweets)
    if sweets < 1:
        context.bot.send_message(update.effective_chat.id,f'Ура! Победил игрок {flag}')
        return ConversationHandler.END
    else:
        flag = 1
        context.bot.send_message(update.effective_chat.id, f'Осталось {sweets} конфет.\n Теперь'
                                                                f'ходит игрок {flag}')
        print('second flag == 1')
        return FIRST 


def cancel(update, context):
    print('my cancel started')
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END

start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
first_handler = MessageHandler(Filters.text, first)
second_handler = MessageHandler(Filters.text, second)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                     states={
                                         FIRST: [first_handler],
                                         SECOND: [second_handler],
                                     },
                                     fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()