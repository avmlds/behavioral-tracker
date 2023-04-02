import io
from copy import deepcopy
from datetime import datetime, timedelta
from typing import List, Union, Dict, Optional

import numpy as np
import matplotlib

matplotlib.use("agg")  # noqa

import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter
from matplotlib.ticker import FormatStrFormatter
from sqlalchemy import func
from telebot.types import InputMediaPhoto

from app.constants import key_texts, CALLBACK_TEXT_MAP
from app.constants.key_texts import MOOD_IMPACT_MAP
from app.controllers import BaseController
from app.models import UserMood, Mood, Spectrum, Activity


class ChartController(BaseController):
    __base_model__ = UserMood
    __sub_model__ = Mood
    __support_model__ = Spectrum
    __activity_model__ = Activity

    MOOD_TITLE = key_texts.MOOD
    DISPOSITION_TITLE = key_texts.DISPOSITION
    PRODUCTIVITY_TITLE = key_texts.PRODUCTIVITY
    CONFIDENCE_TITLE = key_texts.CONFIDENCE

    SIMPLE_CHART_TITLES = [
        MOOD_TITLE,
        DISPOSITION_TITLE,
        PRODUCTIVITY_TITLE,
        CONFIDENCE_TITLE,
    ]

    @staticmethod
    def save_to_buf(plot):
        buf = io.BytesIO()
        plot.savefig(buf, format="png")
        buf.seek(0)
        data = buf.read()
        buf.close()
        return data

    @staticmethod
    def min_max_scaler(
        left_border: Union[int, float],
        right_border: Union[int, float],
        values: List[int],
    ):
        """MinMaxScaler."""

        if left_border >= right_border:
            raise Exception("Incorrect scale range")

        minimum = min(values)
        maximum = max(values)

        if minimum >= left_border and maximum <= right_border:
            return values

        if minimum == maximum:
            # Possible only when all values equal
            target_value = min([max([left_border, values[0]]), right_border])
            return [target_value for _ in range(len(values))]

        values_stds = [(i - minimum) / (maximum - minimum) for i in values]
        return [i * (right_border - left_border) + left_border for i in values_stds]

    @staticmethod
    def standard_scaler(values: List[int]):
        mean = sum(values) / len(values)
        std = (sum((x - mean) ** 2 for x in values) / 4) ** 0.5
        return [(value - mean) / std for value in values]

    @classmethod
    def horizontal_bar_chart(cls, titles: List[str], values: List[Union[int, float]]):
        fig, ax = plt.subplots()

        interval_min = -2
        interval_max = 2
        graph_min = [interval_min for _ in range(len(values))]
        graph_max = [interval_max for _ in range(len(values))]

        bar_height = 0.3
        label_gap = 0.05
        y_pos = [0, 0.5, 1, 1.5]

        scaled_values = [i / max([abs(min(values)), abs(max(values))]) for i in values]

        ax.barh(
            y_pos,
            scaled_values,
            align="center",
            edgecolor="black",
            color="black",
            height=bar_height,
            alpha=0.5,
        )
        ax.barh(
            y_pos,
            graph_min,
            align="center",
            edgecolor="black",
            color="white",
            alpha=0.2,
            height=bar_height,
        )
        ax.barh(
            y_pos,
            graph_max,
            align="center",
            edgecolor="black",
            color="white",
            alpha=0.2,
            height=bar_height,
        )

        ax.set(yticklabels=[])
        ax.tick_params(left=False)

        for y, title in zip(y_pos, titles):
            ax.text(x=0, y=y - (bar_height / 2) - label_gap, s=title, ha="center")

        ax.invert_yaxis()
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)
        return cls.save_to_buf(plt)

    @classmethod
    def polar_pie_chart(
        cls, values: Dict[str, Union[int, float]], plot_title: Optional[str] = None
    ) -> bytes:
        labels = []
        impacts = []
        for label, value in values.items():
            labels.append(label)
            impacts.append(value)

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))

        labels.append(labels[0])
        impacts.append(impacts[0])

        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(polar=True)
        colors = plt.cm.cividis(angles / 5)
        ax.bar(angles, impacts, width=0.7, color=colors, edgecolor="black")
        ax.set_yticklabels([])
        ax.set_thetagrids(angles * 180 / np.pi, labels)
        ax.tick_params(pad=10, labelsize=8)
        ax.spines["polar"].set_visible(False)
        plt.grid(True)
        plt.tight_layout(pad=3)
        if plot_title:
            plt.suptitle(plot_title)

        return cls.save_to_buf(plt)

    @classmethod
    def reason_chart(cls, values: Dict[str, Union[int, float]]):
        labels = []
        impacts = []
        for label, value in values.items():
            labels.append(label)
            impacts.append(value)

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))

        labels.append(labels[0])
        impacts.append(impacts[0])

        fig = plt.figure()
        ax = fig.add_subplot(polar=True)  # basic plot

        ax.plot(angles, impacts, "o--", color="g")
        ax.fill(angles, impacts, alpha=0.2, color="g")

        ax.set_yticklabels([])
        ax.set_thetagrids(angles * 180 / np.pi, labels)
        ax.tick_params(pad=30)
        ax.spines["polar"].set_visible(False)
        plt.grid(True)
        plt.tight_layout()
        return cls.save_to_buf(plt)

    @classmethod
    def mood_oscillation_chart(
        cls,
        values: Dict[str, Dict[datetime, Union[int, float]]],
        date_formatter: DateFormatter,
        chart_type: str,
    ):
        fig, axes = plt.subplots(figsize=(8, 8), nrows=4, sharex="all")
        for label, ax in zip(cls.SIMPLE_CHART_TITLES, axes):
            chart_values = sorted(values[label].items(), key=lambda x: x[0])
            timestamps = [i[0] for i in chart_values]
            impact = [i[1] for i in chart_values]

            ax.scatter(timestamps, impact)
            ax.plot(timestamps, impact, "o--")
            ax.axhline(color="black", lw=0.5)
            ax.set_ylabel(label, loc="center")
            ax.xaxis.set_major_formatter(date_formatter)
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
            ax.grid(True)

        plt.autoscale(False)
        plt.subplots_adjust(hspace=0.2)
        fig.autofmt_xdate()
        plt.suptitle(f"{chart_type} chart")
        plt.tight_layout(pad=2)
        return cls.save_to_buf(plt)

    def create_monthly_mood_oscillation_chart(self, user_id):
        today = datetime.now()
        one_month_ago = today - timedelta(days=30)

        items = (
            self._connection.query(
                func.date_trunc("day", UserMood.created_at),
                Mood.callback,
                func.sum(Spectrum.weight),
            )
            .join(Spectrum, UserMood.spectrum_id == Spectrum.id)
            .join(Mood, Spectrum.mood_id == Mood.id)
            .filter(UserMood.user_id == user_id)
            .filter(func.date_trunc("day", UserMood.created_at) >= one_month_ago)
            .group_by(func.date_trunc("day", UserMood.created_at), Mood.callback)
            .order_by(func.date_trunc("day", UserMood.created_at))
            .all()
        )
        chart_values = {
            key: {(today - timedelta(days=x)).date(): 0 for x in range(30)}
            for key in self.SIMPLE_CHART_TITLES
        }

        for timestamp, callback_name, value in items:
            key = CALLBACK_TEXT_MAP[callback_name]
            chart_values[key][timestamp.date()] = value
        return self.mood_oscillation_chart(
            chart_values, DateFormatter("%d-%m-%Y"), chart_type="Monthly"
        )

    def create_weekly_mood_oscillation_chart(self, user_id):
        today = datetime.now()
        one_week_ago = today - timedelta(weeks=1)

        items = (
            self._connection.query(
                func.date_trunc("day", UserMood.created_at),
                Mood.callback,
                func.sum(Spectrum.weight),
            )
            .join(Spectrum, UserMood.spectrum_id == Spectrum.id)
            .join(Mood, Spectrum.mood_id == Mood.id)
            .filter(UserMood.user_id == user_id)
            .filter(func.date_trunc("day", UserMood.created_at) >= one_week_ago)
            .group_by(func.date_trunc("day", UserMood.created_at), Mood.callback)
            .order_by(func.date_trunc("day", UserMood.created_at))
            .all()
        )
        chart_values = {
            key: {(today - timedelta(days=x)).date(): 0 for x in range(7)}
            for key in self.SIMPLE_CHART_TITLES
        }

        for timestamp, callback_name, value in items:
            key = CALLBACK_TEXT_MAP[callback_name]
            chart_values[key][timestamp.date()] = value
        return self.mood_oscillation_chart(
            chart_values, DateFormatter("%d-%m-%Y"), chart_type="Weekly"
        )

    def create_daily_mood_oscillation_chart(self, user_id):
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        items = (
            self._connection.query(
                func.date_trunc("minute", UserMood.created_at),
                Mood.callback,
                func.sum(Spectrum.weight),
            )
            .join(Spectrum, UserMood.spectrum_id == Spectrum.id)
            .join(Mood, Spectrum.mood_id == Mood.id)
            .filter(UserMood.user_id == user_id)
            .filter(func.date_trunc("minute", UserMood.created_at) >= yesterday)
            .group_by(func.date_trunc("minute", UserMood.created_at), Mood.callback)
            .order_by(func.date_trunc("minute", UserMood.created_at))
            .all()
        )
        chart_values = {
            key: {today - timedelta(hours=x): 0 for x in range(today.hour)}
            for key in self.SIMPLE_CHART_TITLES
        }

        for timestamp, callback_name, value in items:
            key = CALLBACK_TEXT_MAP[callback_name]
            chart_values[key][timestamp] = value
        return self.mood_oscillation_chart(
            chart_values, DateFormatter("%H:%M"), chart_type="Daily"
        )

    def create_reason_chart_by_category(self, user_id):
        # [
        #     ('CONFIDENCE_CALLBACK', 'FAMILY_CALLBACK', 1),
        #     ('DISPOSITION_CALLBACK', 'ENVIRONMENT_CALLBACK', 1),
        #     ('DISPOSITION_CALLBACK', 'FAMILY_CALLBACK', 1),
        #     ('DISPOSITION_CALLBACK', 'STUDY_CALLBACK', 1),
        #     ('MOOD_CALLBACK', 'HEALTH_CALLBACK', 3),
        #     ('MOOD_CALLBACK', 'SOCIAL_CALLBACK', 1),
        #     ('MOOD_CALLBACK', 'STUDY_CALLBACK', 1),
        #     ('PRODUCTIVITY_CALLBACK', 'SOCIAL_CALLBACK', 1)
        # ]

        items = (
            self._connection.query(
                Mood.callback, Activity.callback, func.count(UserMood.id)
            )
            .filter(UserMood.user_id == user_id)
            .join(Spectrum, UserMood.spectrum_id == Spectrum.id)
            .join(Mood, Spectrum.mood_id == Mood.id)
            .join(Activity, UserMood.activity_id == Activity.id)
            .group_by(Mood.callback, Activity.callback)
            .all()
        )

        data = deepcopy(MOOD_IMPACT_MAP)
        for mood_callback, reason_callback, impact_score in items:
            mood_callback_key = CALLBACK_TEXT_MAP[mood_callback]
            data[mood_callback_key].update(
                {CALLBACK_TEXT_MAP[reason_callback]: impact_score}
            )

        items = []
        for mood_callback, reason in data.items():
            title = f"Things that affect your {mood_callback}"
            items.append(InputMediaPhoto(media=self.polar_pie_chart(reason, title)))
        return items
