from telebot.types import InlineKeyboardMarkup

from app.constants import states, key_callbacks
from app.controllers import FeedbackController
from app.keyboard.system import FeedbackKeyboard, StartKeyboard
from app.templates.system import FEEDBACK_TEMPLATE, FEEDBACK_ANSWER_TEMPLATE
from app.views.base import MessageBaseView, QueryBaseView


class QueryFeedbackView(QueryBaseView):

    __query__ = key_callbacks.FEEDBACK_CALLBACK

    def _response_text(self) -> str:
        return FEEDBACK_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return FeedbackKeyboard()

    def answer(self):
        self._edit_message()
        self.controller.update_user_state(states.FEEDBACK_STATE, message=self.message)
        self.controller.append_to_user_state_data(
            message=self.message,
            data=key_callbacks.FEEDBACK_CALLBACK,
        )


class FeedbackView(MessageBaseView):

    __state__ = states.FEEDBACK_STATE

    def _response_text(self) -> str:
        return FEEDBACK_ANSWER_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return StartKeyboard()

    def answer(self):
        feedback_controller = FeedbackController(connection=self.connection)
        feedback_controller.insert(
            feedback=self.message.text, user_id=self.message.chat.id
        )
        self._send_message()
        self.controller.update_user_state(states.IDLE_STATE, message=self.message)
        self.controller.update_user_state_data(
            message=self.message,
            data=key_callbacks.START_CALLBACK,
        )
