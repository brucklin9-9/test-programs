import telebot
from telebot import types
#import config

bot = telebot.TeleBot("1663399217:AAHUbla9zvsaYbRIyihCWE-2uXHB3KH1dgs")

@bot.message_handler(commands=['start'])
def send_start(message):
#	markup = types.
	bot.reply_to(message, "Привет, я твой помошник.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
