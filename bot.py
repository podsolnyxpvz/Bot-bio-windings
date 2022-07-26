import telebot
import random
import requests
from requests import get
from telebot import types

bot=telebot.TeleBot("5412471687:AAFAa6s3iCMcTmJD3b75VmaxaFQYROg7RxY")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url='https://t.me/windingsss')
    button2 = types.InlineKeyboardButton("𝙱𝙸𝙾", url='https://t.me/+zkP_CTwKviViOTAy')
    button3 = types.InlineKeyboardButton("𝙶𝙸𝚃𝙷𝚄𝙱", url='https://github.com/podsolnyxpvz')
    button4 = types.InlineKeyboardButton("𝚅𝙺 𝙼𝚄𝚂𝙸𝙲 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃", url='https://vk.com/music/playlist/572449584_15_6efb7499cb6273c9fa')
    button5 = types.InlineKeyboardButton("𝚃𝙸𝙺 𝚃𝙾𝙺", url='tiktok.com/@anlcho')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

bot.infinity_polling(none_stop=True)