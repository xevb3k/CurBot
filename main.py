import telebot
import requests
import json
from config import TOKEN, keys
from extension import ConvertionException, Convert

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    text = 'Для конвертации введите команду в следующем формате: \
        \nЧерез пробел и без скобок: <имя валюты из какой переводим> <в какую валюту переводим> <количество> \
        \nПоказать список доступных валют через команду /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    text = 'Привет! \
        \nЭто бот для конвертации валют: \
        \n- показать список доступных валют через команду /values \
        \n- конвертировать (без скобок через пробел) <из какой> <в какую> <количество> \
        \n- помощь /help'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split()

        if len(values) != 3:
            raise ConvertionException('Количество параметров должно быть равно 3')

        quote, base, amount = values
        result = Convert.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.send_message(message.chat.id, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка\n{e}')
    else:
        text = f'{amount} "{quote}" ({keys[quote]})   =   {result} "{base}" ({keys[base]})'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)


