from telebot.types import InlineKeyboardMarkup

from app.constants.key_callbacks import (
    BALANCE_WHEEL_CHART_CALLBACK,
    MONTHLY_TIME_CHART_CALLBACK,
    WEEKLY_TIME_CHART_CALLBACK,
    DAILY_TIME_CHART_CALLBACK,
    INSIGHTS_CALLBACK,
)
from app.controllers.image_controller import ChartController
from app.keyboard.insights import InsightsKeyboard, ChartInsightsKeyboard
from app.templates.insights import (
    INSIGHTS_SECTION_TEMPLATE,
    INSIGHTS_DAILY_TIME_CHART,
    INSIGHTS_WEEKLY_TIME_CHART,
    INSIGHTS_MONTHLY_TIME_CHART,
    INSIGHTS_BALANCE_WHEEL_CHART,
)
from app.views.base import QueryBaseView


class InsightsView(QueryBaseView):
    __query__ = INSIGHTS_CALLBACK

    def _response_text(self) -> str:
        return INSIGHTS_SECTION_TEMPLATE

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return InsightsKeyboard()

    def answer(self):
        self._edit_message()
        self.update_last_state()


class DailyTimeChartView(QueryBaseView):
    __query__ = DAILY_TIME_CHART_CALLBACK

    def _response_text(self) -> str:
        return INSIGHTS_DAILY_TIME_CHART

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return ChartInsightsKeyboard()

    def _response_picture(self):
        controller = ChartController(connection=self.connection)
        return controller.create_daily_mood_oscillation_chart(self.message.chat.id)

    def answer(self):
        self._send_picture()
        self._send_message()
        self.update_last_state()


class WeeklyTimeChartView(DailyTimeChartView):
    __query__ = WEEKLY_TIME_CHART_CALLBACK

    def _response_text(self) -> str:
        return INSIGHTS_WEEKLY_TIME_CHART

    def _response_picture(self):
        controller = ChartController(connection=self.connection)
        return controller.create_weekly_mood_oscillation_chart(self.message.chat.id)


class MonthlyTimeChartView(DailyTimeChartView):
    __query__ = MONTHLY_TIME_CHART_CALLBACK

    def _response_text(self) -> str:
        return INSIGHTS_MONTHLY_TIME_CHART

    def _response_picture(self):
        controller = ChartController(connection=self.connection)
        return controller.create_monthly_mood_oscillation_chart(self.message.chat.id)


class BalanceWheelChartView(QueryBaseView):
    __query__ = BALANCE_WHEEL_CHART_CALLBACK

    def _response_text(self) -> str:
        return INSIGHTS_BALANCE_WHEEL_CHART

    def _media_group(self):
        """Media group to send."""

        controller = ChartController(connection=self.connection)
        return controller.create_reason_chart_by_category(self.message.chat.id)

    def _response_keyboard(self) -> InlineKeyboardMarkup:
        return ChartInsightsKeyboard()

    def answer(self):
        self._send_media_group()
        self._send_message()
        self.update_last_state()
