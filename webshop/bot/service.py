from typing import List

from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from .lookups import CATEGORY_LOOKUP, SEPARATOR
from ..db.models import Category


class WebShopBot(TeleBot):

    def generate_categories_kb(self, categories: List[Category], **kwargs):
        kb = InlineKeyboardMarkup(**kwargs)
        buttons = [InlineKeyboardButton(
            text=c.title,
            callback_data=f'{CATEGORY_LOOKUP}{SEPARATOR}{c.id}'
        ) for c in categories]
        kb.add(*buttons)

        return kb

    def generate_and_send_categories_kb(self, text: str, chat_id: int,
                                        categories: List[Category], **kwargs):
        self.send_message(chat_id, text, reply_markup=self.generate_categories_kb(categories, **kwargs))

    def generate_and_edit_categories_kb(self, text: str, chat_id: int,
                                        message_id: int, categories: List[Category], **kwargs):
        self.edit_message_text(
            text,
            chat_id,
            message_id,
            reply_markup=self.generate_categories_kb(categories, **kwargs))


