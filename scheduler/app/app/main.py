import os
import logging
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer

import telebot
from telebot.types import BotCommand, Message, CallbackQuery

from app.controllers import (
    Keyboard,
    UserController,
)

import app.constants.states as states
from app.controllers.base import get_session

from app.controllers.category_controller import CategoryController
from app.controllers.feedback_controller import FeedbackController

from app.templates import START_TEMPLATE, HELP_TEMPLATE

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

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
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


@bot.message_handler(commands=["start"], content_types=["text"])
@get_session
def handle_start(message, session):
    logger.info(
        f"User {message.chat.id} pressed start or help, state updated to IDLE_STATE"
    )
    UserController(connection=session).update_user_state(states.IDLE_STATE, message)
    return bot.send_message(
        message.chat.id, START_TEMPLATE, reply_markup=Keyboard.default_keyboard()
    )


@bot.message_handler(commands=["help"], content_types=["text"])
@get_session
def handle_start(message, session):
    logger.info(
        f"User {message.chat.id} pressed start or help, state updated to IDLE_STATE"
    )
    UserController(connection=session).update_user_state(states.IDLE_STATE, message)
    return bot.send_message(
        message.chat.id, HELP_TEMPLATE, reply_markup=Keyboard.default_keyboard()
    )


@bot.callback_query_handler(lambda query: query.data in Keyboard.CATEGORIES)
@get_session
def select_category(query: CallbackQuery, session):
    message = query.message
    logger.info(
        f"User {message.chat.id} pressed {query.data}, state updated to IDLE_STATE"
    )
    UserController(connection=session).update_user_state(
        user_state=states.CHOOSE_CATEGORY_STATE, message=message
    )
    return bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.id,
        text="""Choose subcategory""",
        reply_markup=Keyboard.build_keyboard(
            [Keyboard.GO_BACK] + Keyboard.CATEGORIES_MAP[query.data]
        ),
    )


@bot.callback_query_handler(lambda query: query.data in Keyboard.ALL_CATEGORIES)
@get_session
def submit_subcategory(query: CallbackQuery, session):
    message = query.message
    logger.info(f"User {message.chat.id} submitting subcategory.")
    CategoryController(connection=session).insert(query.data, message.chat.id)
    UserController(connection=session).update_user_state(
        user_state=states.CHOOSE_SUBCATEGORY_STATE, message=message
    )
    return bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.id,
        text="""Successfully added""",
        reply_markup=Keyboard.default_keyboard(),
    )


@bot.callback_query_handler(lambda query: query.data in (Keyboard.GO_BACK,))
@get_session
def go_back(query: CallbackQuery, session):
    message = query.message
    logger.info(f"User {message.chat.id} pressed go_back.")
    UserController(connection=session).update_user_state(
        user_state=states.IDLE_STATE, message=message
    )
    return bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.id,
        text=START_TEMPLATE,
        reply_markup=Keyboard.default_keyboard()
    )


@bot.callback_query_handler(lambda query: query.data in (Keyboard.SUBMIT_FEEDBACK,))
@get_session
def submit_feedback(query: CallbackQuery, session):
    """Submit feedback to database."""

    message = query.message
    UserController(connection=session).update_user_state(
        user_state=states.FEEDBACK_STATE, message=message
    )
    return bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.id,
        text=(
            "We highly encourage you to take a few moments to "
            "write down your suggestions and feedback about our product, "
            "as your input is incredibly valuable in helping us improve and "
            "meet your needs more effectively.\n\nThank you for your contribution!"
        ),
        reply_markup=Keyboard.go_back_keyboard(),
    )


@bot.message_handler()
@get_session
def operate_messages(message: Message, session):
    user_id = chat_id = message.chat.id

    user_controller = UserController(connection=session)
    user_state = user_controller.get_user_state(message)

    if user_state is None:
        logger.info(f"User {message.chat.id} sent message without state, new user")
        return bot.send_message(
            chat_id, START_TEMPLATE, reply_markup=Keyboard.default_keyboard()
        )

    elif user_state == states.IDLE_STATE:
        logger.info(f"User {message.chat.id} sent message in IDLE_STATE")
        return bot.send_message(
            chat_id, START_TEMPLATE, reply_markup=Keyboard.default_keyboard()
        )

    elif user_state == states.FEEDBACK_STATE:
        logger.info(f"User {message.chat.id} sent message in FEEDBACK_STATE")

        feedback_controller = FeedbackController(connection=session)
        feedback_controller.insert(feedback=message.text, user_id=user_id)
        UserController(connection=session).update_user_state(
            user_state=states.IDLE_STATE, message=message
        )
        return bot.send_message(
            chat_id=message.chat.id,
            text=(
                "Thank you for sharing your feedback with us - we truly "
                "appreciate your contribution in helping us improve our product.\n\n"
                "We will carefully review your suggestions and take them "
                "into consideration as we work to make our product even better for you."
            ),
            reply_markup=Keyboard.default_keyboard(),
        )

    else:
        logger.error(f"User {message.chat.id} sent message in UNKNOWN STATE")
        return bot.send_message(
            message.chat.id, START_TEMPLATE, reply_markup=Keyboard.default_keyboard()
        )


if __name__ == "__main__":
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
