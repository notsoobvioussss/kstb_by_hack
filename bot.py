import telebot

# Создаем экземпляр бота

bot = telebot.TeleBot('5272235435:AAHpP-PpRGuy1CAnAnug3-zxLW7lZcW2Wnw')

# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start"])

def start(m, res=False):

    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

# Получение сообщений от юзера

@bot.message_handler(content_types=["text"])

def handle_text(message):
    if 'дела' in message.text.lower():
        bot.send_message(message.chat.id, 'Хорошо)')
    elif 'здрав' in message.text.lower():
        bot.send_message(message.chat.id, 'Здравствуйте!')
    elif 'прив' in message.text.lower():
        bot.send_message(message.chat.id, 'Привет!')
    elif 'адрес' in message.text.lower():
        bot.send_message(message.chat.id, 'г. Казань, ул. Деревни Универсиады,  д. 32')
    elif 'телефон' in message.text.lower():
        bot.send_message(message.chat.id, '77777777777')



# Запускаем бота

bot.polling(none_stop=True, interval=0)