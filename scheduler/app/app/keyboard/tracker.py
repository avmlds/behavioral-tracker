from app.constants import buttons
from app.keyboard.base import Keyboard


class TrackerKeyboard(Keyboard):
    __buttons__ = [
        [buttons.MOOD_BUTTON, buttons.DISPOSITION_BUTTON],
        [buttons.PRODUCTIVITY_BUTTON, buttons.CONFIDENCE_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]


class MoodKeyboard(Keyboard):
    __buttons__ = [
        [buttons.HAPPY_BUTTON],
        [buttons.CONTENT_BUTTON],
        [buttons.NEUTRAL_BUTTON],
        [buttons.DISAPPOINTED_BUTTON],
        [buttons.DEPRESSED_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]


class DispositionKeyboard(Keyboard):
    __buttons__ = [
        [buttons.CALM_BUTTON],
        [buttons.FRUSTRATED_BUTTON],
        [buttons.IRRITATED_BUTTON],
        [buttons.ANNOYED_BUTTON],
        [buttons.ANGRY_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]


class ProductivityKeyboard(Keyboard):
    __buttons__ = [
        [buttons.PRODUCTIVE_BUTTON],
        [buttons.MOTIVATED_BUTTON],
        [buttons.INDECISIVE_BUTTON],
        [buttons.OVERWHELMED_BUTTON],
        [buttons.PROCRASTINATING_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]


class ConfidenceKeyboard(Keyboard):
    __buttons__ = [
        [buttons.CONFIDENT_BUTTON],
        [buttons.APPREHENSIVE_BUTTON],
        [buttons.NERVOUS_BUTTON],
        [buttons.STRESSED_BUTTON],
        [buttons.ANXIOUS_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]


class ReasonKeyboard(Keyboard):
    __buttons__ = [
        [buttons.HEALTH_BUTTON],
        [buttons.CHORES_BUTTON],
        [buttons.WORK_BUTTON],
        [buttons.STUDY_BUTTON],
        [buttons.MYSELF_BUTTON],
        [buttons.ENVIRONMENT_BUTTON],
        [buttons.SOCIAL_BUTTON],
        [buttons.RELATIONSHIP_BUTTON],
        [buttons.FAMILY_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]
