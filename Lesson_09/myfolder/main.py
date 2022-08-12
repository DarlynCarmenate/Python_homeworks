from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd

bot = Bot(token='5505014803:AAHY7A-AwN6Q_gCgVeln7gepH1R_dtTEnIQ')
updater = Updater(token='5505014803:AAHY7A-AwN6Q_gCgVeln7gepH1R_dtTEnIQ')
dispatcher = updater.dispatcher


def start(update, context):
    text = 'Давай начнем играть в крестики-нолики. Выбирай номер строки и столбца для Х'
    arr[0][0] = '*'
    arr[0][1] = '*'
    arr[0][2] = '*'
    arr[1][0] = '*'
    arr[1][1] = '*'
    arr[1][2] = '*'
    arr[2][0] = '*'
    arr[2][1] = '*'
    arr[2][2] = '*'
    context.bot.send_message(update.effective_chat.id, text + '\n' + arr_to_str(arr))

def bot_hod(array):
    x = rd(0, 2)
    y = rd(0, 2)
    while array[x][y] != '*':
        x = rd(0, 2)
        y = rd(0, 2)
    return [x, y]

def hody(update, context):
    text = update.message.text
    data = text.split(',')
    arr[int(data[0]) - 1][int(data[1]) - 1] = 'X'
    if arr[0][0] == arr[0][1] == arr[0][2] != '*' or arr[1][0] == arr[1][1] == arr[1][2] != '*' or \
    arr[2][0] == arr[2][1] == arr[2][2] != '*' or arr[0][0] == arr[1][0] == arr[2][0] != '*' or \
    arr[0][1] == arr[1][1] == arr[2][1] != '*' or arr[0][2] == arr[1][2] == arr[2][2] != '*' or \
    arr[0][0] == arr[1][1] == arr[2][2] != '*' or arr[0][2] == arr[1][1] == arr[2][0] != '*':
        output = arr_to_str(arr) + 'Ты победил!'
    elif not_in_arr(arr):
        output = arr_to_str(arr) + 'Ничья!'
    else:
        output = arr_to_str(arr) + 'Теперь мой ход \n'
        data = bot_hod(arr)
        arr[int(data[0])][int(data[1])] = 'O'
        print(arr_to_str(arr))
        if arr[0][0] == arr[0][1] == arr[0][2] != '*' or arr[1][0] == arr[1][1] == arr[1][2] != '*' or \
        arr[2][0] == arr[2][1] == arr[2][2] != '*' or arr[0][0] == arr[1][0] == arr[2][0] != '*' or \
        arr[0][1] == arr[1][1] == arr[2][1] != '*' or arr[0][2] == arr[1][2] == arr[2][2] != '*' or \
        arr[0][0] == arr[1][1] == arr[2][2] != '*' or arr[0][2] == arr[1][1] == arr[2][0] != '*':
            output = arr_to_str(arr) + 'Я победил!'
        elif not_in_arr(arr):
            output = arr_to_str(arr) + 'Ничья!'
        else:
            output += arr_to_str(arr) + 'Теперь твой ход'
    context.bot.send_message(update.effective_chat.id, output)

def arr_to_str(arr):
    result = ''
    for i in range(3):
        for j in range(3):
            result += arr[i][j] + ' '
        result += '\n'
    return result

def not_in_arr(arr):
    for i in arr:
        for j in i:
            if j == '*':
                return False
    return True

# def message(update, context):
#     text = update.message.text
#     print(text)
#     context.bot.send_message(update.effective_chat.id, "Как же вы мне надоели!")

arr = [['*', '*', '*'], 
       ['*', '*', '*'], 
       ['*', '*', '*']]
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, hody)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()