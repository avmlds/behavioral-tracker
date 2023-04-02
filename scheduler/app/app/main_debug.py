import logging

from telebot.types import Message, CallbackQuery

import app.constants.states as states
from app.constants import key_callbacks
from app.controllers import UserController
from app.controllers.base import get_session
from app.core.server import bot, start_polling
from app.views.base import MessageViewRegistry, QueryViewRegistry

logger = logging.getLogger()


@bot.message_handler(commands=["start"], content_types=["text"])
@get_session
def handle_start(message, session):
    MessageViewRegistry[states.IDLE_STATE](
        bot, message, controller=UserController(connection=session)
    ).answer()


@bot.message_handler(commands=["help"], content_types=["text"])
@get_session
def handle_help(message, session):
    QueryViewRegistry[key_callbacks.HELP_CALLBACK](
        bot, message, controller=UserController(connection=session)
    ).answer()


@bot.callback_query_handler(lambda query: query.data in QueryViewRegistry)
@get_session
def select_category(query: CallbackQuery, session):
    message = query.message
    data = query.data

    user_controller = UserController(connection=session)
    klass = QueryViewRegistry[data]
    klass(bot, message, data, controller=user_controller, db_session=session).answer()


@bot.message_handler()
@get_session
def operate_messages(message: Message, session):
    # TODO: Delete messages sent by user
    user_controller = UserController(connection=session)
    user_state = user_controller.get_user_state(message)

    klass = MessageViewRegistry[user_state]
    if not klass:
        klass = MessageViewRegistry[states.IDLE_STATE]

    klass(bot, message, controller=user_controller, db_session=session).answer()


if __name__ == "__main__":
    start_polling()
