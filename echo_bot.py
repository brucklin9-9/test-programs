import telebot

bot = telebot.TeleBot("1663399217:AAHUbla9zvsaYbRIyihCWE-2uXHB3KH1dgs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Вы сделали запрос старт или помощь.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message.text)

bot.infinity_polling()
