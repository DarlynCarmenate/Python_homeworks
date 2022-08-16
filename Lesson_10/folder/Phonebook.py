# Создать телефонный справочник на импорт и экспорт в тг-боте

from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from russian_names import RussianNames as rn
from random import randint as rd


bot = Bot(token='5497396012:AAH8ECTfz-jqVEmCHmdXb1voAsaSk90cbDE')
updater = Updater(token='5497396012:AAH8ECTfz-jqVEmCHmdXb1voAsaSk90cbDE')
dispatcher = updater.dispatcher

NAME_DATA = 0
TEL_DATA = 1
CITY_DATA = 2
RESULT = 4
d = dict()

def create_dict():
    lst = ['Москва', 'Адлер', 'Сочи', 'СПб', 'Москва', 'Чита', 'Омск', 'Ейск', 'Тверь', 'Тула']
    d = dict()
    for i in range(10):
        d[i] = rn(patronymic = False).get_person(), f'+7-{rd(200, 500)}-{rd(100000000,199999999)}', lst[i] 
    return d

def dict_write():
    with open('dict.txt','w', encoding='utf-8') as out:
        for key,val in d.items():
            out.write('{}:{}\n'.format(key,val))
    out.close()

d = create_dict()
dict_write()

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро подаловать в телефонный справочник!'
                                                       'Если хочешь прочесть данные введи /export\n'
                                                       'А если записать, введи /import: ')


def export(update, context):
    board = [InlineKeyboardButton('Горизонтально', callback_data='0'), 
            InlineKeyboardButton('Вертикально', callback_data='1')],
    context.bot.send_message(update.effective_chat.id,'Как лучше распечатать?', reply_markup=InlineKeyboardMarkup(board))


def operation(update, context):
    que = update.callback_query
    var = que.data
    que.answer()
    if var == '0':
        que.edit_message_text(print_horizontal(d))
    elif var == '1':
        que.edit_message_text(print_vertical(d))

def print_vertical(d):
    res = ''
    for i in range(len(d)):
        res += f'ФИО {d[i][0]} \n Тел. {d[i][1]} \n Город {d[i][2]}; \n'
    return res

def print_horizontal(d):
    res = ''
    for i in range(len(d)):
        res += f'{i+1} {d[i][0]} {d[i][1]} {d[i][2]}; '
    return res

def name_data(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите ФИО нового контакта: ')
    return TEL_DATA

def tel_data(update, context):
    global new_name
    new_name = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введите телефон контакта: ')
    return CITY_DATA

def city_data(update, context):
    global new_tel
    new_tel = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введите город контакта: ')
    return RESULT

def result_data(update, context):
    global new_city
    new_city = update.message.text
    d[len(d)] = new_name, new_tel, new_city
    dict_write()
    context.bot.send_message(update.effective_chat.id, print_vertical(d))


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
export_handler = CommandHandler('export', export)
oper_handler = CallbackQueryHandler(operation)
name_handler = CommandHandler('import', name_data)
tel_handler = MessageHandler(Filters.text, tel_data)
city_handler = MessageHandler(Filters.text, city_data)
res_handler = MessageHandler(Filters.text, result_data)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(export_handler)
dispatcher.add_handler(oper_handler)
conv_handler = ConversationHandler(entry_points=[name_handler],
                                     states={
                                         TEL_DATA: [tel_handler],
                                         CITY_DATA: [city_handler],
                                         RESULT: [res_handler],
                                     },
                                     fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()