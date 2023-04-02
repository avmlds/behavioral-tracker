from telebot.types import InlineKeyboardMarkup, InputFile

from app.constants import key_callbacks
from app.controllers.mood import MoodController
from app.keyboard.system import StartKeyboard
from app.keyboard.tracker import (
    TrackerKeyboard,
    MoodKeyboard,
    ProductivityKeyboard,
    DispositionKeyboard,
    ConfidenceKeyboard,
    ReasonKeyboard,
)
from app.templates.confidence import CONFIDENCE_TEMPLATE
from app.templates.disposition import DISPOSITION_TEMPLATE
from app.templates.productivity import PRODUCTIVITY_TEMPLATE
from app.templates.reason import REASON_TEMPLATE
from app.templates.tracker import TRACKER_TEMPLATE, FINISH_TRACKING_TEMPLATE
from app.templates.mood import MOOD_TEMPLATE
from app.views.base import QueryBaseView


class TrackerView(QueryBaseView):
    __query__ = key_callbacks.TRACK_CALLBACK

    def _response_text(self) -> str:
        return TRACKER_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return TrackerKeyboard()

    def answer(self):
        self._edit_message()
        self.update_last_state()


class MoodView(TrackerView):
    __query__ = key_callbacks.MOOD_CALLBACK

    def _response_text(self) -> str:
        return MOOD_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return MoodKeyboard()


class ProductivityView(TrackerView):
    __query__ = key_callbacks.PRODUCTIVITY_CALLBACK

    def _response_text(self) -> str:
        return PRODUCTIVITY_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return ProductivityKeyboard()


class DispositionView(TrackerView):
    __query__ = key_callbacks.DISPOSITION_CALLBACK

    def _response_text(self) -> str:
        return DISPOSITION_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return DispositionKeyboard()


class ConfidenceView(TrackerView):
    __query__ = key_callbacks.CONFIDENCE_CALLBACK

    def _response_text(self) -> str:
        return CONFIDENCE_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return ConfidenceKeyboard()


class ReasonView(TrackerView):
    __query__ = key_callbacks.REASON_CAUSE_CALLBACKS

    def _response_text(self) -> str:
        return REASON_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return ReasonKeyboard()

    def answer(self):
        self._edit_message()
        last_state = self.controller.get_last_user_state_data_item(self.message)
        if last_state != self.query_data:
            self.controller.append_to_user_state_data(self.message, self.query_data)


class AfterReasonView(TrackerView):
    __query__ = key_callbacks.AFTER_REASON_CALLBACKS

    def _response_text(self) -> str:
        return FINISH_TRACKING_TEMPLATE

    def _response_picture(self) -> InputFile:
        pass

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return StartKeyboard()

    def answer(self):
        mood_callback, spectrum_callback = self.controller.get_mood_callbacks(
            self.message
        )
        mood_controller = MoodController(connection=self.connection)
        mood_controller.insert(
            mood_callback, spectrum_callback, self.query_data, message=self.message
        )

        self._edit_message()

        self.controller.update_user_state_data(
            message=self.message, data=key_callbacks.START_CALLBACK
        )
