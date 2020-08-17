from .config import TOKEN, DEFAULT_PHOTO_URL
from .keyboards import START_KB, ADD_TO_CART
from .lookups import PRODUCT_LOOKUP, SEPARATOR, CATEGORY_LOOKUP
from ..db.models import Text, Product, Category

from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from .service import WebShopBot

bot_instance = WebShopBot(TOKEN)


@bot_instance.message_handler(commands=['start'])
def start(message):

    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [KeyboardButton(button) for button in START_KB.values()]
    kb.add(*buttons)

    txt = 'Здравствуй, дорогой пользователь. Рад тебя приветсвовать в нашем магазине!'

    bot_instance.send_message(
        message.chat.id,
        txt,
        reply_markup=kb
    )






"""
"Clients: web, mobile" <-> "Web servers: Apache, Nginx, Tomcat, Caddy" <->
"wsgi server: gunicorn, unicorn, cherrypy" <-> "python app"
"""