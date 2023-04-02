import datetime
import logging
from typing import Optional

from telebot.types import Message

from app.controllers import BaseController
from app.models.users import BotUser, UserState

logger = logging.getLogger(__name__)


class StateController(BaseController):
    __base_model__ = UserState

    def one_by_user_id(self, user_id: int) -> UserState:
        return (
            self._connection.query(self.__base_model__)
            .filter(self.__base_model__.user_id == user_id)
            .first()
        )

    def update_state(self, *, user_id: int, user_state: str) -> UserState:

        user_state_model = self.one_by_user_id(user_id)
        if not user_state_model:
            user_state_model = self.create(
                user_id=user_id,
                user_state=user_state,
                updated_at=datetime.datetime.now(),
            )
        else:
            user_state_model.user_state = user_state
            user_state_model.updated_at = datetime.datetime.now()
            self._connection.commit()
            self._connection.refresh(user_state_model)
        return user_state_model

    def update_state_data(
        self, *, message: Message, user_state_data: str, meta: Optional[dict] = None
    ) -> UserState:
        user_state_model = self.one_by_user_id(message.chat.id)

        user_state_data_json = {"data": user_state_data}
        if meta:
            user_state_data_json.update({"meta": meta})
        user_state_model.user_state_data = user_state_data_json

        user_state_model.updated_at = datetime.datetime.now()
        self._connection.commit()
        self._connection.refresh(user_state_model)
        return user_state_model

    def get_state_by_user(self, message: Message):
        return self.one_by_user_id(message.chat.id).user_state

    def get_state_data_by_user(self, user_id: int) -> dict:
        return self.one_by_user_id(user_id).user_state_data


class UserController(BaseController):
    __base_model__ = BotUser

    def __init__(self, connection):
        # TODO: Is it a good idea?
        super().__init__(connection=connection)
        self.state_controller = StateController(connection=connection)

    def one_by_user_chat_id(self, message: Message) -> BotUser:
        return (
            self._connection.query(self.__base_model__)
            .filter(self.__base_model__.id == message.chat.id)
            .first()
        )

    def get_user(self, message: Message) -> BotUser:
        user = self.one_by_user_chat_id(message=message)
        if not user:
            user = self.create(
                id=message.chat.id,
                name=message.chat.first_name,
                login=message.chat.username,
            )
        return user

    def get_user_state(self, message: Message):
        self.get_user(message=message)
        return self.state_controller.get_state_by_user(message)

    def get_user_state_data(self, message: Message) -> dict:
        user = self.get_user(message=message)
        return self.state_controller.get_state_data_by_user(user.id)

    def check_user_state(self, message: Message, user_state: str):
        return self.get_user_state(message=message) == user_state

    def insert_user_state(self, message: Message, user_state: str):
        user = self.get_user(message=message)
        new_state = self.state_controller.create(user_id=user.id, user_state=user_state)
        return new_state

    def update_user_state(self, user_state: str, message: Message):
        user = self.get_user(message=message)
        return self.state_controller.update_state(
            user_id=user.id, user_state=user_state
        )

    def check_user_in_database(self, message: Message):
        return self.get_user(message=message)

    def update_user_state_data(
        self, message: Message, data: str, meta: Optional[dict] = None
    ):
        return self.state_controller.update_state_data(
            message=message, user_state_data=data, meta=meta
        )
