# Made by Ali

import telebot
from decouple import config


BOT_TOKEN = config('BOT_TOKEN')


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start","help"])
def start(message):
    bot.send_message(message.chat.id,"Welcome To The bot!")
    
    
bot.polling()