from webshop.bot import bot_instance
from flask import Flask, abort
from flask import request
from .webshop.bot.config import WEBHOOK_PREFIX, WEBHOOK_URL
from telebot.types import Update

app = Flask(__name__)


@app.route(WEBHOOK_PREFIX, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot_instance.process_new_updates([update])
        return ''
    else:
        abort(403)


if __name__ == '__main__':
    bot_instance.set_webhook(
        url=WEBHOOK_URL,
        certificate=open('webhook_cert.pem', 'r')
    )