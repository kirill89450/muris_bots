import telebot
import config
from datetime import datetime

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['time'])
def time(message):
    time_now = datetime.now().time()
    bot.send_message(message.chat.id, "Сейчас  <b>%d:%d</b>" % (time_now.hour, time_now.minute),
                     parse_mode="HTML")


@bot.message_handler(commands=['date'])
def time(message):
    date_now = datetime.now().date()
    bot.send_message(message.chat.id, "Сегодня  <b>%d.%d.%d</b>" % (date_now.day, date_now.month, date_now.year),
                     parse_mode="HTML")


bot.polling(none_stop=True)
