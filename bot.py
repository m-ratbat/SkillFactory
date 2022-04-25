import telebot
from config import keys, TOKEN
from extensions import ConvertionExeption, CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите комманду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=["values"])
def value (message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Слишком много параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base,amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка со стороны пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        fin_price = float(amount)*float(total_base)
        text = f'Цена {amount} {quote} в {base} - {fin_price}'
        bot.send_message(message.chat.id, text)


bot.polling()
