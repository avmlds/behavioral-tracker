from telebot.types import InlineKeyboardMarkup

from app.constants import states
from app.constants import key_callbacks
from app.keyboard.system import StartKeyboard
from app.templates.system import START_TEMPLATE, HELP_TEMPLATE
from app.views.base import MessageBaseView, QueryBaseView, QueryViewRegistry


class StartView(MessageBaseView):

    __state__ = states.IDLE_STATE

    def _response_text(self) -> str:
        return START_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return StartKeyboard()

    def answer(self):
        self.controller.update_user_state(states.IDLE_STATE, message=self.message)
        self._send_message()
        self.controller.update_user_state_data(
            message=self.message, data=key_callbacks.START_CALLBACK
        )


class QueryStartView(QueryBaseView):

    __query__ = key_callbacks.START_CALLBACK

    def _response_text(self) -> str:
        return START_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return StartKeyboard()

    def answer(self):
        self.controller.update_user_state(states.IDLE_STATE, message=self.message)
        self._edit_message()
        self.controller.update_user_state_data(
            message=self.message, data=key_callbacks.START_CALLBACK
        )


class QueryMainMenuView(QueryStartView):

    __query__ = key_callbacks.MAIN_MENU_CALLBACK


class GoBackView(QueryBaseView):
    __query__ = key_callbacks.GO_BACK_CALLBACK

    def answer(self):
        self.controller.pop_from_user_state_data(self.message)
        last_callback = self.controller.pop_from_user_state_data(self.message)
        QueryViewRegistry[last_callback](
            self.bot,
            self.message,
            controller=self.controller,
        ).answer()


class QueryHelpView(QueryStartView):
    __query__ = key_callbacks.HELP_CALLBACK

    def _response_text(self) -> str:
        return HELP_TEMPLATE

    def answer(self):
        # TODO: Decorator?
        self.controller.update_user_state(states.IDLE_STATE, message=self.message)
        self._send_message()
        self.controller.update_user_state_data(
            message=self.message, data=key_callbacks.START_CALLBACK
        )
