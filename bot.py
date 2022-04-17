import telebot
from telebot import types  # для указание типов
import config
import requests

# Создаем экземпляр бота
massiv = list()
bot = telebot.TeleBot('5272235435:AAHpP-PpRGuy1CAnAnug3-zxLW7lZcW2Wnw')
URL = "https://kastybiy.herokuapp.com"


# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start", "help"])
def welcome(message):
    hello = bot.send_message(message.chat.id, "Сезне сәламлим!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk = types.KeyboardButton("Халык ашлар")
    mrk1 = types.KeyboardButton("Суыткыч")
    mrk2 = types.KeyboardButton("Яраткан ашлар")
    markup.add(mrk, mrk1, mrk2)
    bot.send_message(message.chat.id, "Сайлагыз менюга, бу сезгә кызык", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == "Халык ашлар":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1 = types.KeyboardButton('Камыр ризыклары')
        mar2 = types.KeyboardButton('Беренче ашамлыклар')
        mar3 = types.KeyboardButton('Икенче ашамлыклар')
        mar4 = types.KeyboardButton("Артка")
        markup1.add(mar1, mar2, mar3, mar4)

        bot.send_message(message.chat.id,
                         "Сайлагыз, бу сезгә кирәк, әгәр теләсәгез кайтырга меню гади төймәгә басыгыз 'Артка' ",
                         reply_markup=markup1)
    elif message.text == 'Камыр ризыклары':
        a = [0, 2, 3, 8, 9, 13, 14]
        data = requests.get(URL + "/api/get/cuisine").json()
        for i in a:
            id = data[i]['id']
            title = data[i]['title']
            cookSteps = data[i]['cookSteps']
            cookTime = data[i]['cookTime']
            source = data[i]['source']
            calories = data[i]['calories']
            proteins = data[i]['proteins']
            fats = data[i]['fats']
            carboh = data[i]['carboh']
            products = data[i]['products']
            products = products[1:].split('*')
            products = ', '.join(products)
            cookSteps = cookSteps.split('\\n')
            cookSteps = '\n'.join(cookSteps)
            mes = f'{title} \nНеобходимые продукты: {products} \n' \
                  f'Рецепт:\n{cookSteps}\nВремя готовки: {cookTime} минут. \n' \
                  f'Калории: {calories} ккал. \nБелки: {proteins} г. \nЖиры:{fats} г. \nУглеводы:{carboh} г. \n' \
                  f'{source}'
            bot.send_photo(message.chat.id, photo=f"https://lafoy.ru/photo_l/foto-1626-{id}.jpg")
            bot.send_message(message.chat.id,
                             mes)
        bot.send_message(message.chat.id,
                         "Если вам понравилось какое-либо блюдо, то введите его название, как оно указано в рецепте")

    elif message.text == 'Беренче ашамлыклар':
        a = [5, 7, 11]
        data = requests.get(URL + "/api/get/cuisine").json()
        for i in a:
            id = data[i]['id']
            title = data[i]['title']
            cookSteps = data[i]['cookSteps']
            cookTime = data[i]['cookTime']
            source = data[i]['source']
            calories = data[i]['calories']
            proteins = data[i]['proteins']
            fats = data[i]['fats']
            carboh = data[i]['carboh']
            products = data[i]['products']
            products = products[1:].split('*')
            products = ', '.join(products)
            cookSteps = cookSteps.split('\\n')
            cookSteps = '\n'.join(cookSteps)
            mes = f'{title} \nНеобходимые продукты: {products} \n' \
                  f'Рецепт:\n{cookSteps}\nВремя готовки: {cookTime} минут. \n' \
                  f'Калории: {calories} ккал. \nБелки: {proteins} г. \nЖиры:{fats} г. \nУглеводы:{carboh} г. \n' \
                  f'{source}'
            bot.send_photo(message.chat.id, photo=f"https://lafoy.ru/photo_l/foto-1626-{id}.jpg")
            bot.send_message(message.chat.id,
                             mes)
            bot.send_message(message.chat.id,
                             "Если вам понравилось какое-либо блюдо, то введите его название, как оно указано в рецепте")
    elif message.text == 'Икенче ашамлыклар':
        a = [1, 4, 6, 10, 12]
        data = requests.get(URL + "/api/get/cuisine").json()
        for i in a:
            id = data[i]['id']
            title = data[i]['title']
            cookSteps = data[i]['cookSteps']
            cookTime = data[i]['cookTime']
            source = data[i]['source']
            calories = data[i]['calories']
            proteins = data[i]['proteins']
            fats = data[i]['fats']
            carboh = data[i]['carboh']
            products = data[i]['products']
            products = products[1:].split('*')
            products = ', '.join(products)
            cookSteps = cookSteps.split('\\n')
            cookSteps = '\n'.join(cookSteps)
            mes = f'{title} \nНеобходимые продукты: {products} \n' \
                  f'Рецепт:\n{cookSteps}\nВремя готовки: {cookTime} минут. \n' \
                  f'Калории: {calories} ккал. \nБелки: {proteins} г. \nЖиры:{fats} г. \nУглеводы:{carboh} г. \n' \
                  f'{source}'
            bot.send_photo(message.chat.id, photo=f"https://lafoy.ru/photo_l/foto-1626-{id}.jpg")
            bot.send_message(message.chat.id,
                             mes)
            bot.send_message(message.chat.id,
                             "Если вам понравилось какое-либо блюдо, то введите его название, как оно указано в рецепте")
    elif message.text == 'Суыткыч':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar2 = types.KeyboardButton("Артка")
        markup1.add(mar2)
        bot.send_message(message.chat.id,
                         "Сайлагыз, бу сезгә кирәк, әгәр теләсәгез кайтырга меню гади төймәгә басыгыз 'Артка' ",
                         reply_markup=markup1)
        data = requests.get(URL + "/api/get/products").json()
        s = ''
        for i in data:
            id = i['id']
            name = i['name']
            s += f'{id}. {name}\n'
        bot.send_message(message.chat.id,
                         s)
        bot.send_message(message.chat.id,
                         "Введите номера продуктов из списка через пробел")
    elif message.text == 'Яраткан ашлар':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar2 = types.KeyboardButton("Артка")
        markup1.add(mar2)
        bot.send_message(message.chat.id,
                         "Сайлагыз, бу сезгә кирәк, әгәр теләсәгез кайтырга меню гади төймәгә басыгыз 'Артка' ",
                         reply_markup=markup1)
        bot.send_message(message.chat.id,
                         "Ваши любимые блюда:")
        s = ''
        for i in massiv:
            s+= i
            s +='\n'
        bot.send_message(message.chat.id,
                         s)

    elif message.text[0] in '0123456789':
        data = requests.get(URL + "/api/get/cuisine").json()
        mes = message.text
        mes = mes.split(' ')
        mes.sort()
        mes = ''.join(mes)
        s = ''
        for i in data:
            itog = i['itogProducts']
            itog = itog.split('*')
            itog.sort()
            itog = ''.join(itog)
            title = i['title']
            category = i['category']
            if itog == mes:
                s += f'Вы можете приготовить: {title} Раздел: {category}\n'
        if s == '':
            bot.send_message(message.chat.id, "Недостаточно продуктов для приготвления любого блюда")
        else:
            bot.send_message(message.chat.id, s)
    elif message.text == "Артка":
        welcome(message)
    else:
        s = message.text
        data = requests.get(URL + "/api/get/cuisine").json()
        for i in data:
            title = i['title']
            category = i['category']
            if title == s:
                massiv.append(f'{title} Раздел: {category}')






# Запускаем бота


bot.polling(none_stop=True, interval=0)
