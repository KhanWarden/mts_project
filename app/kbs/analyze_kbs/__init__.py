from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .columns_to_analyse_kb import (ColumnsCallback, columns_kb)

__all__ = ['analyze_data_kb',
           'ColumnsCallback',
           'columns_kb']


def analyze_data_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Максимальные значения", callback_data="max_values")],
        [InlineKeyboardButton(text="Среднее значение", callback_data="avg_values")],
        [InlineKeyboardButton(text="Минимальные значения", callback_data="min_values")],
        [InlineKeyboardButton(text="Корреляция между колонками", callback_data="correlation")],
        [InlineKeyboardButton(text="Рассчитать коэфф. продуктивности", callback_data="productivity")],
        [InlineKeyboardButton(text="Самый лучший студент", callback_data="best_student")],
        [InlineKeyboardButton(text="Самый вовлеченный студент", callback_data="engaged_student")],
        [InlineKeyboardButton(text="Самая сложная категория уроков", callback_data="difficult_lesson")],
        [InlineKeyboardButton(text="В меню", callback_data="to_menu")]
    ])
    return inline_kb