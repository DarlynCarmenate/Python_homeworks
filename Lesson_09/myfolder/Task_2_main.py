# Создать калькулятор для работы с рациональными и комплексными числами, 
# организовать меню, добавив в неё систему логирования

from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from Task_2_commands import *

    
bot = Bot(token='5379008886:AAE967v5PulUzUkCtTHnXv7jdariyJn4FPs')
updater = Updater(token='5379008886:AAE967v5PulUzUkCtTHnXv7jdariyJn4FPs')
dispatcher = updater.dispatcher

def start(update, context):
  log(update, context)
  context.bot.send_message(update.effective_chat.id, f'Привет, {update.effective_user.first_name}! Я могу посчитать рациональные или полные комплексные числа. Введи пример, используй пробелы: ')
  # context.bot.send_message(update.effective_chat.id,'Привет')

def calc_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  #myout = calc(msg)
  context.bot.send_message(update.effective_chat.id, calc(msg) )


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, calc_command)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()