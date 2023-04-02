from typing import List

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Keyboard(InlineKeyboardMarkup):

    __buttons__: List[InlineKeyboardButton] = [[]]
    __row_width__: int = 1

    def __init__(self):
        super().__init__(keyboard=self.__buttons__, row_width=self.__row_width__)
