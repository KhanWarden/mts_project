from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pandas.core.interchange import column


class MaxColumnsCallback(CallbackData, prefix="max_columns_callback"):
    name: str


class MinColumnsCallback(CallbackData, prefix="min_columns_callback"):
    name: str


class AverageColumnsCallback(CallbackData, prefix="avg_columns_callback"):
    name: str


columns = ('Accuracy', 'Rhythm', 'Tempo', 'Pitch Accuracy', 'Duration', 'Volume', 'Heart Rate',
           'Blood Pressure', 'Focus Time', 'Performance Score', 'Engagement Score')


def max_columns_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=column,
                              callback_data=MaxColumnsCallback(name=column.replace(" ", "_")).pack())]
        for column in columns
    ])
    return inline_kb


def min_columns_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=column,
                              callback_data=MinColumnsCallback(name=column.replace(" ", "-")).pack())]
        for column in columns
    ])
    return inline_kb


def avg_columns_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=column,
                              callback_data=AverageColumnsCallback(name=column.replace(" ", ".")).pack())]
        for column in columns
    ])
    return inline_kb
