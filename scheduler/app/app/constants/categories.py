"""Categories and subcategories that used in keyboards."""

PHYSICAL_HEALTH_CATEGORY = "Physical Health"
MENTAL_HEALTH_CATEGORY = "Mental Health"
HOUSEHOLD_CHORES_CATEGORY = "Household Chores"
WORK_CATEGORY = "Work"
STUDY_CATEGORY = "Study"
PERSONAL_LIFE_CATEGORY = "Personal Life"
MOOD_CATEGORY = "Mood"

PHYSICAL_HEALTH_ACTIVITIES = [
    "Drink water",
    "Take vitamins/medications",
    "Stretch",
    "Go for a walk/run",
    "Practice yoga/pilates",
    "Strength training",
    "Go to the gym",
    "Take a nap",
    "Get some fresh air",
    "Have sex",
    "Do exercises",
]

MENTAL_HEALTH_ACTIVITIES = [
    "Practice gratitude",
    "Journal",
    "Talk to a friend",
    "Talk to a therapist/counselor",
    "Take a break from work/study",
    "Read a book",
    "Play video games",
]

HOUSEHOLD_CHORES_ACTIVITIES = [
    "Do laundry",
    "Clean the kitchen",
    "Vacuum",
    "Dust",
    "Organize/clean out a closet",
    "Water plants",
    "Clean the bathroom",
    "Take out the trash",
    "Wash dishes",
    "Cook meals",
    "Eat meals",
    "Go grocery shopping",
    "Go clothes shopping",
    "Get a haircut",
]

WORK_ACTIVITIES = [
    "Attend a meeting",
    "Complete a project/task",
    "Check in with a colleague",
    "Update a to-do list",
    "Attend a networking event",
    "Participate in professional development",
    "Prepare for a presentation",
    "Check work email",
]

STUDY_ACTIVITIES = [
    "Attend a class",
    "Complete an assignment",
    "Research for a paper/assignment",
    "Study for an exam",
]

PERSONAL_LIFE_ACTIVITIES = [
    "Check social medias",
    "Watch a movie/TV show",
    "Listen to a podcast",
    "Have a date night",
    "Spend time with family",
    "Have alone time",
    "Travel/explore a new place",
    "Volunteer for a cause",
    "Make plans with friends",
    "Hang out with friends",
    "Meet with relatives",
    "Go out for a meal",
]


MOOD_ACTIVITIES = [
    "Happy",
    "Content",
    "Neutral",
    "Anxious",
    "Stressed",
    "Overwhelmed",
    "Sad",
    "Depressed",
    "Angry",
    "Irritated",
    "Frustrated",
    "Grateful",
    "Joyful",
    "Excited",
    "Tired",
    "Restless",
    "Productive",
    "Accomplished",
    "Confident",
    "Hopeful",
]


CATEGORIES_MAP = {
    PHYSICAL_HEALTH_CATEGORY: PHYSICAL_HEALTH_ACTIVITIES,
    MENTAL_HEALTH_CATEGORY: MENTAL_HEALTH_ACTIVITIES,
    HOUSEHOLD_CHORES_CATEGORY: HOUSEHOLD_CHORES_ACTIVITIES,
    WORK_CATEGORY: WORK_ACTIVITIES,
    STUDY_CATEGORY: STUDY_ACTIVITIES,
    PERSONAL_LIFE_CATEGORY: PERSONAL_LIFE_ACTIVITIES,
    MOOD_CATEGORY: MOOD_ACTIVITIES,
}


"""

PHYSICAL_HEALTH_CATEGORY = "Physical Health \U0001F3CB"
MENTAL_HEALTH_CATEGORY = "Mental Health \U0001F9D8"
HOUSEHOLD_CHORES_CATEGORY = "Household Chores \U0001F9F9"
WORK_CATEGORY = "Work \U0001F4BC"
STUDY_CATEGORY = "Study \U0001F4DA"
PERSONAL_LIFE_CATEGORY = "Personal Life \U0001F9D1\U0001F91D\U0001F9D1"
MOOD_CATEGORY = "Mood \U0001F60A"


PHYSICAL_HEALTH_ACTIVITIES = [
    "Drink water \U0001F4A7",
    "Take vitamins/medications \U0001F48A",
    "Stretch \U0001F646",
    "Go for a walk/run \U0001F3C3",
    "Practice yoga/pilates \U0001F9D8",
    "Strength training \U0001F3CB",
    "Go to the gym‍️ \U0001F3CB",
    "Take a nap \U0001F4A4",
    "Get some fresh air️ \U0001F32C",
    "Have sex \U0001F491",
    "Do exercises \U0001F3CB",
]

MENTAL_HEALTH_ACTIVITIES = [
    "Practice gratitude \U0001F64F",
    "Journal \U0001F4DD",
    "Talk to a friend \U0001F5E3",
    "Talk to a therapist/counselor \U0001F9D1",
    "Take a break from work/study \U0001F334",
    "Read a book \U0001F4D6",
    "Play video games \U0001F3AE",
]

HOUSEHOLD_CHORES_ACTIVITIES = [
    "Do laundry \U0001F9FA",
    "Clean the kitchen \U0001F9FC",
    "Vacuum \U0001F9F9",
    "Dust \U0001FA9E",
    "Organize/clean out a closet \U0001F9F9\U0001F455",
    "Water plants \U0001F331\U0001F4A7",
    "Clean the bathroom \U0001F6BD\U0001F9FC",
    "Take out the trash \U0001F5D1",
    "Wash dishes \U0001F37D\U0001F9FC",
    "Cook meals \U0001F373\U0001F468\U0001F373",
    "Eat meals \U0001F37D\U0001F374",
    "Go grocery shopping \U0001F6D2",
    "Go clothes shopping \U0001F455\U0001F456",
    "Get a haircut \U0001F487",
]

WORK_ACTIVITIES = [
    "Attend a meeting \U0001F465",
    "Complete a project/task \U0001F3AF",
    "Check in with a colleague \U0001F91D",
    "Update a to-do list \U0001F4DD",
    "Attend a networking event \U0001F4E1",
    "Participate in professional development \U0001F4DA",
    "Prepare for a presentation \U0001F3A4",
    "Check work email \U0001F4E7",
]

STUDY_ACTIVITIES = [
    "Attend a class \U0001F3EB",
    "Complete an assignment \U0001F4DD",
    "Research for a paper/assignment \U0001F50D",
    "Study for an exam \U0001F4DA",
]

PERSONAL_LIFE_ACTIVITIES = [
    "Check social medias \U0001F4F1",
    "Watch a movie/TV show \U0001F3AC",
    "Listen to a podcast \U0001F3A7",
    "Have a date night \U00002764\U0001F469\U0001F469\U00002764",
    "Spend time with family \U0001F46A",
    "Have alone time \U0001F9D8",
    "Travel/explore a new place \U0001F30D\U00002708",
    "Volunteer for a cause \U0001F91D",
    "Make plans with friends \U0001F4C5",
    "Hang out with friends \U0001F37B",
    "Meet with relatives \U0001F468\U0001F469\U0001F467\U0001F466",
    "Go out for a meal \U0001F37D",
]


MOOD_ACTIVITIES = [
    "Happy \U0001F600",
    "Content \U0001F642",
    "Neutral \U0001F610",
    "Anxious \U0001F630",
    "Stressed \U0001F625",
    "Overwhelmed \U0001F629",
    "Sad \U0001F622",
    "Depressed \U0001F625\U0000FE0F\U0000200D\U0001F4AB",
    "Angry \U0001F621",
    "Irritated \U0001F644",
    "Frustrated \U0001F620",
    "Grateful \U0001F64F\U0000200D\U0000270C\U0001F64F",
    "Joyful \U0001F604",
    "Excited \U0001F929",
    "Tired \U0001F62B",
    "Restless \U0001F644\U0000200D\U0001F300",
    "Productive \U0001F4AA",
    "Accomplished \U0001F389",
    "Confident \U0001F44F\U0000200D\U00002640\U0000FE0F",
    "Hopeful \U0001F64F\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D0",
]


CATEGORIES_MAP = {
    PHYSICAL_HEALTH_CATEGORY: PHYSICAL_HEALTH_ACTIVITIES,
    MENTAL_HEALTH_CATEGORY: MENTAL_HEALTH_ACTIVITIES,
    HOUSEHOLD_CHORES_CATEGORY: HOUSEHOLD_CHORES_ACTIVITIES,
    WORK_CATEGORY: WORK_ACTIVITIES,
    STUDY_CATEGORY: STUDY_ACTIVITIES,
    PERSONAL_LIFE_CATEGORY: PERSONAL_LIFE_ACTIVITIES,
    MOOD_CATEGORY: MOOD_ACTIVITIES,
}

"""
