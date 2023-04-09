import telebot
from pars import *
from telebot import types
from Globals import *
import random


TOKEN = get_token()


bot = telebot.TeleBot(TOKEN)

g = get_url()


def next_anime():
    global g
    g = get_url()
    anime.parse(g)


anime = Anime()
anime.parse(g)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🎲Искать рандомные аниме🎲', callback_data='get_anime'))
    bot.send_message(message.chat.id, 'Привет! Это бот для поиска рандомных аниме!', reply_markup=markup)


@bot.message_handler(commands=['get_anime'])
def send_anime(message):
    global anime
    photo = open('img.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Смотреть⏎', url=anime.get_link()))
    markup.add(types.InlineKeyboardButton('Дальше🎲', callback_data='get_anime'))
    markup.add(types.InlineKeyboardButton('Описание🔍', callback_data='get_description'))
    bot.send_message(message.chat.id, f'{anime.get_name()}\nЭпизоды: {anime.get_episodes()}\nРейтинг: {anime.rate}⭐️\nЖанры: {anime.get_genres()}', reply_markup=markup)


@bot.callback_query_handler(func= lambda call: True)
def answ(call):
    if call.data == 'get_anime':
        try:
            next_anime()
            send_anime(call.message)
        except:
            next_anime()
            send_anime(call.message)
    elif call.data == 'get_description':
        anime = Anime()
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=anime.get_description(), reply_markup=markup2)
    elif call.data == 'back':
        anime = Anime()
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Смотреть⏎', url=anime.get_link()))
        markup1.add(types.InlineKeyboardButton('Дальше🎲', callback_data='get_anime'))
        markup1.add(types.InlineKeyboardButton('Описание🔍', callback_data='get_description'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{anime.get_name()}\nЭпизоды: {anime.get_episodes()}\nРейтинг: {anime.rate}⭐️\nЖанры: {anime.get_genres()}', reply_markup=markup1)


bot.infinity_polling()



TOKEN = get_token()


bot = telebot.TeleBot(TOKEN)

g = get_url()


def next_anime():
    global g
    g = get_url()
    anime.parse(g)


anime = Anime()
anime.parse(g)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🎲Искать рандомные аниме🎲', callback_data='get_anime'))
    bot.send_message(message.chat.id, 'Привет! Это бот для поиска рандомных аниме!', reply_markup=markup)


@bot.message_handler(commands=['get_anime'])
def send_anime(message):
    global anime
    photo = open('img.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Смотреть⏎', url=anime.get_link()))
    markup.add(types.InlineKeyboardButton('Дальше🎲', callback_data='get_anime'))
    markup.add(types.InlineKeyboardButton('Описание🔍', callback_data='get_description'))
    bot.send_message(message.chat.id, f'{anime.get_name()}\nЭпизоды: {anime.get_episodes()}\nРейтинг: {anime.rate}⭐️\nЖанры: {anime.get_genres()}', reply_markup=markup)


@bot.callback_query_handler(func= lambda call: True)
def answ(call):
    if call.data == 'get_anime':
        try:
            next_anime()
            send_anime(call.message)
        except:
            next_anime()
            send_anime(call.message)
    elif call.data == 'get_description':
        anime = Anime()
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=anime.get_description(), reply_markup=markup2)
    elif call.data == 'back':
        anime = Anime()
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Смотреть⏎', url=anime.get_link()))
        markup1.add(types.InlineKeyboardButton('Дальше🎲', callback_data='get_anime'))
        markup1.add(types.InlineKeyboardButton('Описание🔍', callback_data='get_description'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{anime.get_name()}\nЭпизоды: {anime.get_episodes()}\nРейтинг: {anime.rate}⭐️\nЖанры: {anime.get_genres()}', reply_markup=markup1)


bot.infinity_polling()

