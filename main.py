import telebot
from pars import *
from telebot import types
from Globals import *
import time
import random


TOKEN = get_token()


bot = telebot.TeleBot(TOKEN)

g = get_url()

f = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]


def next_anime():
    global g
    g = get_url()
    anime.parse(g)


anime = Anime()
anime.parse(g)

di = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Искать', callback_data='get_anime'))
    bot.send_message(message.chat.id, 'Привет! Это бот для поиска рандомных аниме!', reply_markup=markup)


@bot.message_handler(commands=['get_anime'])
def send_anime(message):
    global anime, di
    time.sleep(0.2)
    photo = open('img.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('Смотреть⏎', url=anime.get_link()))
    markup1.add(types.InlineKeyboardButton('Дальше👉', callback_data='get_anime'))
    markup1.add(types.InlineKeyboardButton('Описание🔍', callback_data='get_description'))
    a = f'{anime.get_name()}\nЭпизоды: {anime.get_episodes()}\nРейтинг: {anime.rate}⭐️\nЖанры: {anime.get_genres()}'
    try:
        di[message.chat.id] = [anime.description, a]
    except:
        di[message.chat.id] = [anime.description, a]
    bot.send_message(message.chat.id, a, reply_markup=markup1)


@bot.callback_query_handler(func= lambda call: True)
def answ(call):
    global anime, di
    if call.data == 'get_anime':
        try:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id - 1)
        except:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id - 2)
        next_anime()
        send_anime(call.message)
    elif call.data == 'get_description':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=di[call.message.chat.id][0], reply_markup=markup)
        except:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=di[call.message.chat.id][0], reply_markup=markup)
    elif call.data == 'back':
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Смотреть⏎', url=anime.get_link()))
        markup1.add(types.InlineKeyboardButton('Дальше👉', callback_data='get_anime'))
        markup1.add(types.InlineKeyboardButton('Описание🔍', callback_data='get_description'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=di[call.message.chat.id][1], reply_markup=markup1)


bot.infinity_polling()

