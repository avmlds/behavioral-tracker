"""Module with user states."""


IDLE_STATE = "IDLE_STATE"
CHOOSE_CATEGORY_STATE = "CHOOSE_CATEGORY_STATE"
CHOOSE_SUBCATEGORY_STATE = "CHOOSE_SUBCATEGORY_STATE"
FEEDBACK_STATE = "FEEDBACK_STATE"


ALL_STATES = [
    IDLE_STATE,
    CHOOSE_CATEGORY_STATE,
    CHOOSE_SUBCATEGORY_STATE,
    FEEDBACK_STATE,
]

ALL_STATES_STRING = ",".join(ALL_STATES)
