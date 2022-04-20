import telebot

TOKEN = "5208427203:AAGynpkmTpzZLkpku3XDpXSz6CfgFXASd_Q"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    text = 'Привет! Это бот для конвертации валют:  \n- Показать список доступных валют через команду /values \
        \n- Вывести конвертацию валюты через команду <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
    - Напомнить, что я могу через команду /help'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)


