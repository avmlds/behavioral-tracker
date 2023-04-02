from abc import ABCMeta
from typing import Type, Optional, List

import telebot
from telebot.types import InlineKeyboardMarkup, InputFile, Message, InputMediaPhoto

from app.controllers import UserController


class ViewRegistryMeta(ABCMeta):
    __field_name__ = None
    registry = {}

    def __new__(mcs, name, bases, attrs):
        klass = super(ViewRegistryMeta, mcs).__new__(mcs, name, bases, attrs)
        field_or_fields = getattr(klass, klass.__field_name__, None)
        if field_or_fields is not None:
            if isinstance(field_or_fields, str):
                field_or_fields = [field_or_fields]
            for field in field_or_fields:
                mcs.registry.setdefault(field, klass)

        return klass

    @classmethod
    def __getitem__(mcs, item):
        return mcs.registry.get(item)

    @classmethod
    def __contains__(mcs, item):
        return item in mcs.registry


class QueryViewRegistry(metaclass=ViewRegistryMeta):
    __field_name__ = "__query__"


class MessageViewRegistry(metaclass=ViewRegistryMeta):
    __field_name__ = "__state__"


class BaseMixin:
    """Base mixin class for registry items."""

    def __init__(
        self,
        bot: telebot.TeleBot,
        message: Message,
        query_data: Optional[str] = None,
        locale=None,
        controller=None,
        db_session=None,
    ):
        self.user_controller: Type[UserController] = UserController

        self.bot = bot
        self.query_data = query_data
        self.message: Message = message
        self.locale = locale

        self.controller: UserController = controller
        self.connection = db_session

    def _response_text(self) -> str:
        """Main message of the response."""

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        """Keyboard of the response."""

    def _response_picture(self) -> InputFile:
        """Attachments for the message."""

    def _edit_message(self):
        """Edit message."""

        return self.bot.edit_message_text(
            text=self._response_text(),
            message_id=self.message.message_id,
            chat_id=self.message.chat.id,
            reply_markup=self._response_keyboard(),
        )

    def _photo_caption(self):
        """Caption for the media."""

    def _media_group(self) -> List[InputMediaPhoto]:
        """Media group to send."""

    def _send_media_group(self):
        """Send media group to user."""

        return self.bot.send_media_group(
            chat_id=self.message.chat.id,
            media=self._media_group(),
        )

    def _send_picture(self):
        """Send picture/pictures."""

        return self.bot.send_photo(
            chat_id=self.message.chat.id,
            photo=self._response_picture(),
            caption=self._photo_caption(),
            protect_content=False,
        )

    def _send_message(self):
        """Send message to user."""

        return self.bot.send_message(
            chat_id=self.message.chat.id,
            text=self._response_text(),
            reply_markup=self._response_keyboard(),
            # reply_to_message_id=self.message.message_id,
        )

    def answer(self):
        """General method to act on messages and callbacks."""


class QueryBaseView(QueryViewRegistry, BaseMixin):
    """Base registry for callbacks."""

    __query__ = None

    def __init__(
        self,
        bot: telebot.TeleBot,
        message: Message,
        query_data: Optional[str] = None,
        locale=None,
        controller=None,
        db_session=None,
    ):
        super().__init__(bot, message, query_data, locale, controller, db_session)

    def update_last_state(self):
        last_state = self.controller.get_last_user_state_data_item(self.message)
        if last_state != self.__query__:
            self.controller.append_to_user_state_data(self.message, self.__query__)


class MessageBaseView(MessageViewRegistry, BaseMixin):
    """Base registry for messages."""

    __state__ = None

    def __init__(
        self,
        bot: telebot.TeleBot,
        message: Message,
        query_data: Optional[str] = None,
        locale=None,
        controller=None,
        db_session=None,
    ):
        super().__init__(bot, message, query_data, locale, controller, db_session)
