import logging
import os
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer

import telebot
from telebot.types import BotCommand

logger = logging.getLogger()

formatter = logging.Formatter(
    '%(asctime)s -- %(filename)s -- line_%(lineno)d : "%(message)s"'
)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")
WEBHOOK_PORT = os.environ.get("WEBHOOK_PORT", 443)
WEBHOOK_LISTEN = os.environ.get("WEBHOOK_LISTEN")

WEBHOOK_SSL_CERT = "/app/app/telegram-bot.pem"
WEBHOOK_SSL_PRIV = "/app/app/telegram-bot.key"

WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
WEBHOOK_URL_PATH = f"/{TOKEN}/"


bot = telebot.TeleBot(token=TOKEN, parse_mode="Markdown")
bot.set_my_commands(
    [
        BotCommand("start", description="Start using bot."),
        BotCommand("help", description="Ask for help."),
    ]
)


class WebhookHandler(BaseHTTPRequestHandler):
    server_version = "WebhookHandler/1.0"

    def do_HEAD(self):  # noqa
        self.send_response(200)
        self.end_headers()

    def do_GET(self):  # noqa
        self.send_response(200)
        self.end_headers()

    def do_POST(self):  # noqa
        if (
            self.path == WEBHOOK_URL_PATH
            and "content-type" in self.headers
            and "content-length" in self.headers
            and self.headers["content-type"] == "application/json"
        ):
            json_string = self.rfile.read(int(self.headers["content-length"]))

            self.send_response(200)
            self.end_headers()
            update = telebot.types.Update.de_json(json_string.decode("utf-8"))
            bot.process_new_updates([update])
        else:
            self.send_error(403)
            self.end_headers()


def start_server():
    logger.info("Removing webhook")
    bot.remove_webhook()
    logger.info("Webhook removed, setting webhook")
    bot.set_webhook(
        url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, "r")
    )
    logger.info("Starting httpd")
    httpd = HTTPServer((WEBHOOK_LISTEN, int(WEBHOOK_PORT)), WebhookHandler)
    logger.info("wrapping socket")
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        certfile=WEBHOOK_SSL_CERT,
        keyfile=WEBHOOK_SSL_PRIV,
        server_side=True,
    )
    logger.info("serving")
    httpd.serve_forever()


def start_polling():
    logger.info("Removing webhook")
    bot.remove_webhook()
    bot.infinity_polling()
