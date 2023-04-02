from app.constants import buttons
from app.keyboard.base import Keyboard


class InsightsKeyboard(Keyboard):
    __buttons__ = [
        [buttons.DAILY_TIME_CHART_BUTTON],
        [buttons.WEEKLY_TIME_CHART_BUTTON],
        [buttons.MONTHLY_TIME_CHART_BUTTON],
        [buttons.BALANCE_WHEEL_CHART_BUTTON],
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]


class ChartInsightsKeyboard(Keyboard):
    __buttons__ = [
        [buttons.MAIN_MENU_BUTTON, buttons.GO_BACK_BUTTON],
    ]
