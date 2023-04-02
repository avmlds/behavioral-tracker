from telebot.types import InlineKeyboardButton

from app.constants import key_callbacks, key_texts


class Button(InlineKeyboardButton):
    def __init__(self, text, callback_data):
        super().__init__(text=text, callback_data=callback_data)


TRACK_BUTTON = Button(key_texts.TRACK, key_callbacks.TRACK_CALLBACK)
INSIGHTS_BUTTON = Button(key_texts.INSIGHTS, key_callbacks.INSIGHTS_CALLBACK)
FEEDBACK_BUTTON = Button(key_texts.FEEDBACK, key_callbacks.FEEDBACK_CALLBACK)

MAIN_MENU_BUTTON = Button(key_texts.MAIN_MENU, key_callbacks.MAIN_MENU_CALLBACK)
GO_BACK_BUTTON = Button(key_texts.GO_BACK, key_callbacks.GO_BACK_CALLBACK)

MOOD_BUTTON = Button(key_texts.MOOD, key_callbacks.MOOD_CALLBACK)

HAPPY_BUTTON = Button(key_texts.HAPPY, key_callbacks.HAPPY_CALLBACK)
CONTENT_BUTTON = Button(key_texts.CONTENT, key_callbacks.CONTENT_CALLBACK)
NEUTRAL_BUTTON = Button(key_texts.NEUTRAL, key_callbacks.NEUTRAL_CALLBACK)
DISAPPOINTED_BUTTON = Button(
    key_texts.DISAPPOINTED, key_callbacks.DISAPPOINTED_CALLBACK
)
DEPRESSED_BUTTON = Button(key_texts.DEPRESSED, key_callbacks.DEPRESSED_CALLBACK)

DISPOSITION_BUTTON = Button(key_texts.DISPOSITION, key_callbacks.DISPOSITION_CALLBACK)

CALM_BUTTON = Button(key_texts.CALM, key_callbacks.CALM_CALLBACK)
FRUSTRATED_BUTTON = Button(key_texts.FRUSTRATED, key_callbacks.FRUSTRATED_CALLBACK)
IRRITATED_BUTTON = Button(key_texts.IRRITATED, key_callbacks.IRRITATED_CALLBACK)
ANNOYED_BUTTON = Button(key_texts.ANNOYED, key_callbacks.ANNOYED_CALLBACK)
ANGRY_BUTTON = Button(key_texts.ANGRY, key_callbacks.ANGRY_CALLBACK)

PRODUCTIVITY_BUTTON = Button(
    key_texts.PRODUCTIVITY, key_callbacks.PRODUCTIVITY_CALLBACK
)

PRODUCTIVE_BUTTON = Button(key_texts.PRODUCTIVE, key_callbacks.PRODUCTIVE_CALLBACK)
MOTIVATED_BUTTON = Button(key_texts.MOTIVATED, key_callbacks.MOTIVATED_CALLBACK)
INDECISIVE_BUTTON = Button(key_texts.INDECISIVE, key_callbacks.INDECISIVE_CALLBACK)
OVERWHELMED_BUTTON = Button(key_texts.OVERWHELMED, key_callbacks.OVERWHELMED_CALLBACK)
PROCRASTINATING_BUTTON = Button(
    key_texts.PROCRASTINATING, key_callbacks.PROCRASTINATING_CALLBACK
)

CONFIDENCE_BUTTON = Button(key_texts.CONFIDENCE, key_callbacks.CONFIDENCE_CALLBACK)

CONFIDENT_BUTTON = Button(key_texts.CONFIDENT, key_callbacks.CONFIDENT_CALLBACK)
APPREHENSIVE_BUTTON = Button(
    key_texts.APPREHENSIVE, key_callbacks.APPREHENSIVE_CALLBACK
)
NERVOUS_BUTTON = Button(key_texts.NERVOUS, key_callbacks.NERVOUS_CALLBACK)
STRESSED_BUTTON = Button(key_texts.STRESSED, key_callbacks.STRESSED_CALLBACK)
ANXIOUS_BUTTON = Button(key_texts.ANXIOUS, key_callbacks.ANXIOUS_CALLBACK)

HEALTH_BUTTON = Button(key_texts.HEALTH, key_callbacks.HEALTH_CALLBACK)
CHORES_BUTTON = Button(key_texts.CHORES, key_callbacks.CHORES_CALLBACK)
WORK_BUTTON = Button(key_texts.WORK, key_callbacks.WORK_CALLBACK)
STUDY_BUTTON = Button(key_texts.STUDY, key_callbacks.STUDY_CALLBACK)
MYSELF_BUTTON = Button(key_texts.MYSELF, key_callbacks.MYSELF_CALLBACK)
ENVIRONMENT_BUTTON = Button(key_texts.ENVIRONMENT, key_callbacks.ENVIRONMENT_CALLBACK)
SOCIAL_BUTTON = Button(key_texts.SOCIAL, key_callbacks.SOCIAL_CALLBACK)
FAMILY_BUTTON = Button(key_texts.FAMILY, key_callbacks.FAMILY_CALLBACK)
RELATIONSHIP_BUTTON = Button(
    key_texts.RELATIONSHIP, key_callbacks.RELATIONSHIP_CALLBACK
)

DAILY_TIME_CHART_BUTTON = Button(
    key_texts.DAILY_TIME_CHART, key_callbacks.DAILY_TIME_CHART_CALLBACK
)
WEEKLY_TIME_CHART_BUTTON = Button(
    key_texts.WEEKLY_TIME_CHART, key_callbacks.WEEKLY_TIME_CHART_CALLBACK
)
MONTHLY_TIME_CHART_BUTTON = Button(
    key_texts.MONTHLY_TIME_CHART, key_callbacks.MONTHLY_TIME_CHART_CALLBACK
)
BALANCE_WHEEL_CHART_BUTTON = Button(
    key_texts.BALANCE_WHEEL_CHART, key_callbacks.BALANCE_WHEEL_CHART_CALLBACK
)
