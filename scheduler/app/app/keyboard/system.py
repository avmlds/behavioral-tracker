from app.constants import buttons
from app.keyboard.base import Keyboard


class StartKeyboard(Keyboard):
    __buttons__ = [
        [buttons.TRACK_BUTTON],
        [buttons.FEEDBACK_BUTTON, buttons.INSIGHTS_BUTTON],
    ]


class FeedbackKeyboard(Keyboard):
    __buttons__ = [[buttons.GO_BACK_BUTTON]]
