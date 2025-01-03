from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .columns_to_analyse_kb import (ColumnsCallback, columns_kb)
from .analysis_kb import CallbackForAnalysis, instruments_kb, class_levels_kb

__all__ = ['analyze_data_kb',
           'ColumnsCallback',
           'columns_kb',
           'CallbackForAnalysis',
           'instruments_kb',
           'class_levels_kb',
           'productivity_kb']


def analyze_data_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Максимальные значения", callback_data="max_values")],
        [InlineKeyboardButton(text="Среднее значение", callback_data="avg_values")],
        [InlineKeyboardButton(text="Минимальные значения", callback_data="min_values")],
        [InlineKeyboardButton(text="Корреляция между колонками", callback_data="correlation")],
        [InlineKeyboardButton(text="Рассчитать коэфф. продуктивности", callback_data="productivity")],
        [InlineKeyboardButton(text="Средняя эффективность студента", callback_data="average_perf_score")],
        [InlineKeyboardButton(text="Корреляция между уровнем вовлеченности и развитием навыков",
                              callback_data="correlation_between_two")],
        [InlineKeyboardButton(text="В меню", callback_data="to_menu")]
    ])
    return inline_kb


def productivity_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать всех", callback_data="productivity_all")],
        [InlineKeyboardButton(text="Рассчитать студента", callback_data="productivity_of_student")],
        [InlineKeyboardButton(text="В меню", callback_data="to_menu")]
    ])
    return inline_kb
