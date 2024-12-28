from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .columns_to_analyse_kb import (max_columns_kb, MaxColumnsCallback, min_columns_kb, avg_columns_kb,
                                    MinColumnsCallback, AverageColumnsCallback)

__all__ = ['max_columns_kb',
           'min_columns_kb',
           'avg_columns_kb',
           'analyze_data_kb',
           'MaxColumnsCallback',
           'MinColumnsCallback',
           'AverageColumnsCallback',]


def analyze_data_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Максимальные значения", callback_data="max_values")],
        [InlineKeyboardButton(text="Среднее значение", callback_data="avg_values")],
        [InlineKeyboardButton(text="Минимальные значения", callback_data="min_values")],
        [InlineKeyboardButton(text="Изменить запись", callback_data="change_row")],
        [InlineKeyboardButton(text="Названия колонок", callback_data="unique_columns")],
        [InlineKeyboardButton(text="В меню", callback_data="to_menu")]
    ])
    return inline_kb
