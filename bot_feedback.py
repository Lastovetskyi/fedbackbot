import telebot

bot = telebot.TeleBot('1238373766:AAGinYhHE6QbKg_EY2ZzUGQtvC0RTK2q1zI')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите ваше ссобщение')
    print(message.chat.id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(283960332, message.text)
    bot.send_message(283960332, message.chat.first_name)
    bot.send_message(283960332, message.chat.username)
    bot.send_message(message.chat.id, 'Спасибо, для отправки повторного сообщение нажмите /start')


bot.polling()




