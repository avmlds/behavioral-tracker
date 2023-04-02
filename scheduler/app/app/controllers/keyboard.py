from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.constants.categories import (
    CATEGORIES_MAP,
    MOOD_CATEGORY,
    PHYSICAL_HEALTH_CATEGORY,
    MENTAL_HEALTH_CATEGORY,
    HOUSEHOLD_CHORES_CATEGORY,
    WORK_CATEGORY,
    STUDY_CATEGORY,
    PERSONAL_LIFE_CATEGORY,
)


class Keyboard:

    GO_BACK = "Go back"
    CATEGORIES_MAP = CATEGORIES_MAP
    CATEGORIES = list(CATEGORIES_MAP.keys())
    ALL_CATEGORIES = [
        j for i in CATEGORIES_MAP.values() for j in i
    ]
    SUBMIT_FEEDBACK = "Give Feedback"

    @classmethod
    def build_keyboard(cls, keyboard_items):
        keyboard = InlineKeyboardMarkup()
        keyboard.row_width = 2
        for item in keyboard_items:
            keyboard.add(InlineKeyboardButton(text=item, callback_data=item.rsplit(" ", maxsplit=1)[0]))
        return keyboard

    @classmethod
    def _submit_feedback(cls):
        return InlineKeyboardButton("Feedback \U0001F5E3", callback_data=cls.SUBMIT_FEEDBACK)

    @classmethod
    def default_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES + [cls.SUBMIT_FEEDBACK])

    @classmethod
    def physical_health_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[PHYSICAL_HEALTH_CATEGORY])

    @classmethod
    def mental_health_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[MENTAL_HEALTH_CATEGORY])

    @classmethod
    def household_chores_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[HOUSEHOLD_CHORES_CATEGORY])

    @classmethod
    def work_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[WORK_CATEGORY])

    @classmethod
    def study_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[STUDY_CATEGORY])

    @classmethod
    def personal_life_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[PERSONAL_LIFE_CATEGORY])

    @classmethod
    def mood_keyboard(cls):
        return cls.build_keyboard(cls.CATEGORIES[MOOD_CATEGORY])

    @classmethod
    def go_back_keyboard(cls):
        return cls.build_keyboard([cls.GO_BACK])
