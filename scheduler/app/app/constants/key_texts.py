"""Texts for bot keys."""
from enum import Enum


class Translation(Enum):
    HEALTH = "Health"
    CHORES = "Chores"
    WORK = "Work"
    STUDY = "Study"
    MYSELF = "Myself"
    ENVIRONMENT = "Environment"
    SOCIAL = "Social"
    FAMILY = "Family"
    # ---------------
    # Top-level button
    MOOD = "Mood"
    # Next level buttons
    HAPPY = "Happy"
    CONTENT = "Content"
    NEUTRAL = "Neutral"
    DISAPPOINTED = "Disappointed"
    DEPRESSED = "Depressed"
    # Top-level button
    DISPOSITION = "Disposition"
    # ---------------
    # Next level buttons
    CALM = "Calm"
    FRUSTRATED = "Frustrated"
    IRRITATED = "Irritated"
    ANNOYED = "Annoyed"
    ANGRY = "Angry"
    # Top-level button
    PRODUCTIVITY = "Productivity"
    # ---------------
    # Next level buttons
    PRODUCTIVE = "Productive"
    MOTIVATED = "Motivated"
    INDECISIVE = "Indecisive"
    OVERWHELMED = "Overwhelmed"
    PROCRASTINATING = "Procrastinating"
    # ---------------
    # Top-level button
    CONFIDENCE = "Confidence"
    # Next level buttons
    CONFIDENT = "Confident"
    APPREHENSIVE = "Apprehensive"
    NERVOUS = "Nervous"
    STRESSED = "Stressed"
    ANXIOUS = "Anxious"


class MoodLevels(Enum):
    HAPPY = 2
    CONTENT = 1
    NEUTRAL = 0
    DISAPPOINTED = -1
    DEPRESSED = -2


class DispositionLevels(Enum):
    CALM = 2
    FRUSTRATED = 1
    IRRITATED = 0
    ANNOYED = -1
    ANGRY = -2


class ProductivityLevels(Enum):
    PRODUCTIVE = 2
    MOTIVATED = 1
    INDECISIVE = 0
    OVERWHELMED = -1
    PROCRASTINATING = -2


class ConfidenceLevels(Enum):
    CONFIDENT = 2
    APPREHENSIVE = 1
    NERVOUS = 0
    STRESSED = -1
    ANXIOUS = -2


HEALTH = "Health"
CHORES = "Chores"
WORK = "Work"
STUDY = "Study"
MYSELF = "Myself"
ENVIRONMENT = "Environment"
SOCIAL = "Social"
FAMILY = "Family"
RELATIONSHIP = "Relationship"
# ---------------
# Top-level button
MOOD = "Mood"
# Next level buttons
HAPPY = "Happy"
CONTENT = "Content"
NEUTRAL = "Neutral"
DISAPPOINTED = "Disappointed"
DEPRESSED = "Depressed"
# Top-level button
DISPOSITION = "Disposition"
# ---------------
# Next level buttons
CALM = "Calm"
FRUSTRATED = "Frustrated"
IRRITATED = "Irritated"
ANNOYED = "Annoyed"
ANGRY = "Angry"
# Top-level button
PRODUCTIVITY = "Productivity"
# ---------------
# Next level buttons
PRODUCTIVE = "Productive"
MOTIVATED = "Motivated"
INDECISIVE = "Indecisive"
OVERWHELMED = "Overwhelmed"
PROCRASTINATING = "Procrastinating"
# ---------------
# Top-level button
CONFIDENCE = "Confidence"
# Next level buttons
CONFIDENT = "Confident"
APPREHENSIVE = "Apprehensive"
NERVOUS = "Nervous"
STRESSED = "Stressed"
ANXIOUS = "Anxious"

# Service buttons
GO_BACK = "Go back"

TRACK = "Track"
INSIGHTS = "Insights"
FEEDBACK = "Feedback"
MAIN_MENU = "Main menu"


MOOD_REASONS = [
    HEALTH,
    CHORES,
    WORK,
    STUDY,
    MYSELF,
    ENVIRONMENT,
    SOCIAL,
    FAMILY,
    RELATIONSHIP,
]

MOOD_IMPACT_MAP = {
    MOOD: {r: 0 for r in MOOD_REASONS},
    DISPOSITION: {r: 0 for r in MOOD_REASONS},
    PRODUCTIVITY: {r: 0 for r in MOOD_REASONS},
    CONFIDENCE: {r: 0 for r in MOOD_REASONS},
}

# Insight buttons
DAILY_TIME_CHART = "Daily Time Chart"
WEEKLY_TIME_CHART = "Weekly Time Chart"
MONTHLY_TIME_CHART = "Monthly Time Chart"
BALANCE_WHEEL_CHART = "Balance Wheel Chart"
