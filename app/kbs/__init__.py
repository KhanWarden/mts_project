from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .show_kb import show_kb, pagination_kb
from .analyze_kbs import (analyze_data_kb, max_columns_kb, MaxColumnsCallback, min_columns_kb, avg_columns_kb,
                          MinColumnsCallback, AverageColumnsCallback)


__all__ = ['main_kb',
           'show_kb',
           'pagination_kb',
           'analyze_data_kb',
           'max_columns_kb',
           'min_columns_kb',
           'avg_columns_kb',
           'MaxColumnsCallback',
           'MinColumnsCallback',
           'AverageColumnsCallback',
           'to_menu_kb']


def main_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Просмотреть данные", callback_data="show_data")],
        [InlineKeyboardButton(text="Обработать данные", callback_data="analyze_data")]
    ])
    return inline_kb


def to_menu_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В меню", callback_data="to_menu")]
    ])
    return inline_kb
