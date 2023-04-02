from telebot.types import Message

from app.controllers import BaseController
from app.models import Activity
from app.models.mood import Mood, Spectrum
from app.models.users import UserMood


class MoodController(BaseController):
    __base_model__ = UserMood
    __sub_model__ = Mood
    __support_model__ = Spectrum
    __activity_model__ = Activity

    def __init__(self, connection):
        super().__init__(connection=connection)

    def insert(
        self,
        mood_callback: str,
        spectrum_callback: str,
        reason_callback: str,
        message: Message,
    ):
        mood_id = (
            self._connection.query(self.__sub_model__)
            .filter(self.__sub_model__.callback == mood_callback)
            .first()
            .id
        )
        spectrum_id = (
            self._connection.query(self.__support_model__)
            .filter(self.__support_model__.callback == spectrum_callback)
            .filter(self.__support_model__.mood_id == mood_id)
            .first()
            .id
        )
        activity_id = (
            self._connection.query(self.__activity_model__)
            .filter(self.__activity_model__.callback == reason_callback)
            .first()
            .id
        )
        return self.create(
            user_id=message.chat.id,  # or message.from_user.id ?
            spectrum_id=spectrum_id,
            activity_id=activity_id,
        )
