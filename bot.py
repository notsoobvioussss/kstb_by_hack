import telebot
from telebot import types # для указание типов
import config

# Создаем экземпляр бота

bot = telebot.TeleBot('5272235435:AAHpP-PpRGuy1CAnAnug3-zxLW7lZcW2Wnw')

# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start","help"])
def welcome(message):
    hello = bot.send_message(message.chat.id,"Сезне сәламлим!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk = types.KeyboardButton("Халык ашлары")
    mrk1 = types.KeyboardButton("Суыткыч")
    mrk2 = types.KeyboardButton("Яраткан ашлар")
    markup.add(mrk,mrk1,mrk2)
    bot.send_message(message.chat.id, "Сайлагыз менюга, бу сезгә кызык", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == "Каталог":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar,mar2)
        bot.send_message(message.chat.id,"Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню' ",reply_markup=markup1)
    elif message.text == 'Корзина':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню' ",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        welcome(message)




# Запускаем бота

bot.polling(none_stop=True, interval=0)