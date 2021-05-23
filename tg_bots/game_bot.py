import telebot
import config
from telebot import types
import random
import time

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_dice = types.KeyboardButton("🎲 /dice")
    btn_timer = types.KeyboardButton("⏱ /timer")
    markup.add(btn_dice, btn_timer)
    bot.send_message(message.chat.id, "Привет выбери пункт", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_game(message):
    if message.chat.type == 'private':
        if message.text == "🎲 /dice":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_dice_6 = types.KeyboardButton("Шестигранный 🎲")
            btn_2dice6 = types.KeyboardButton("2 Шестигранных 🎲 ")
            btn_1dice20 = types.KeyboardButton("Двадцатигранный 🎲")
            btn_back = types.KeyboardButton("Назад 🔙")
            markup.add(btn_dice_6, btn_2dice6, btn_1dice20, btn_back)
            bot.send_message(message.chat.id, "Кидай кости", reply_markup=markup)
        elif message.text == ("Назад 🔙"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_dice = types.KeyboardButton("🎲 /dice")
            btn_timer = types.KeyboardButton("⏱ /timer")
            markup.add(btn_dice, btn_timer)
            bot.send_message(message.chat.id, "Привет выбери пункт", reply_markup=markup)
        elif message.text == "⏱ /timer":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_timer30 = types.KeyboardButton("3️⃣0️⃣ сек")
            btn_timer1 = types.KeyboardButton("1️⃣ мин")
            btn_timer5 = types.KeyboardButton("5️⃣ мин")
            btn_back = types.KeyboardButton("Назад 🔙")
            markup.add(btn_timer30, btn_timer1, btn_timer5, btn_back)
            bot.send_message(message.chat.id, 'Засекай время',
                             reply_markup=markup)
        elif message.text == ("3️⃣0️⃣ сек"):
            markstop = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_stop = types.KeyboardButton("🚫")
            markstop.add(btn_stop)
            bot.send_message(message.chat.id, 'засек 30 сек',
                             reply_markup=markstop)
            for i in range(30):
                if message.text == ("🚫"):
                    break
                local_time = float(1)
                time.sleep(local_time)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_timer30 = types.KeyboardButton("3️⃣0️⃣ сек")
            btn_timer1 = types.KeyboardButton("1️⃣ мин")
            btn_timer5 = types.KeyboardButton("5️⃣ мин")
            btn_back = types.KeyboardButton("Назад 🔙")
            markup.add(btn_timer30, btn_timer1, btn_timer5, btn_back)
            bot.send_message(message.chat.id, '30 сек прошло',
                             reply_markup=markup)

        elif message.text == ("1️⃣ мин"):
            markstop = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_stop = types.KeyboardButton("🚫")
            markstop.add(btn_stop)
            bot.send_message(message.chat.id, 'засек 1 минуту',
                             reply_markup=markstop)
            for i in range(60):
                if message.text == ("🚫"):
                    break
                local_time = float(1)
                time.sleep(local_time)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_timer30 = types.KeyboardButton("3️⃣0️⃣ сек")
            btn_timer1 = types.KeyboardButton("1️⃣ мин")
            btn_timer5 = types.KeyboardButton("5️⃣ мин")
            btn_back = types.KeyboardButton("Назад 🔙")
            markup.add(btn_timer30, btn_timer1, btn_timer5, btn_back)
            bot.send_message(message.chat.id, '1 минута прошла',
                             reply_markup=markup)

        elif message.text == ("5️⃣ мин"):
            markstop = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_stop = types.KeyboardButton("🚫")
            markstop.add(btn_stop)
            bot.send_message(message.chat.id, 'засек 5 минут',
                             reply_markup=markstop)
            for i in range(300):
                if message.text == ("🚫"):
                    break
                local_time = float(1)
                time.sleep(local_time)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_timer30 = types.KeyboardButton("3️⃣0️⃣ сек")
            btn_timer1 = types.KeyboardButton("1️⃣ мин")
            btn_timer5 = types.KeyboardButton("5️⃣ мин")
            btn_back = types.KeyboardButton("Назад 🔙")
            markup.add(btn_timer30, btn_timer1, btn_timer5, btn_back)
            bot.send_message(message.chat.id, '5 минут прошло',
                             reply_markup=markup)



        elif message.text == "Шестигранный 🎲":
            number = (random.randint(1, 6))
            bot.send_message(message.chat.id, "Ваше число *%d*" % number, parse_mode='Markdown')
        elif message.text == "2 Шестигранных 🎲":
            number1 = (random.randint(1, 6))
            number2 = (random.randint(1, 6))
            bot.send_message(message.chat.id, "Ваши числа")
            bot.send_message(message.chat.id, "1: *%d*" % number1, parse_mode='Markdown')
            bot.send_message(message.chat.id, "2: *%d*" % number2, parse_mode='Markdown')
        elif message.text == "Двадцатигранный 🎲":
            number = (random.randint(1, 20))
            bot.send_message(message.chat.id, "Ваше число: *%d*" % number, parse_mode='Markdown')


bot.polling(none_stop=True)
