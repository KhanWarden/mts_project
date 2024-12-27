from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .show_kb import show_kb, pagination_kb


__all__ = ['main_kb',
           'show_kb',
           'pagination_kb']


def main_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Просмотреть данные", callback_data="show_data")],
        [InlineKeyboardButton(text="Обработать данные", callback_data="analyze_data")]
    ])
    return inline_kb
