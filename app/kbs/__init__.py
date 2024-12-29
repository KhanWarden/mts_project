from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from .show_kb import show_kb, pagination_kb
from .analyze_kbs import (analyze_data_kb, ColumnsCallback, columns_kb)


__all__ = ['main_kb',
           'show_kb',
           'pagination_kb',
           'analyze_data_kb',
           'ColumnsCallback',
           'columns_kb',
           'to_menu_kb',
           'webapp_kb']


def main_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="See data", callback_data="show_data")],
        [InlineKeyboardButton(text="Analyze data", callback_data="analyze_data")]
    ])
    return inline_kb


def to_menu_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="To Menu", callback_data="to_menu")]
    ])
    return inline_kb


def webapp_kb(values):
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Open in WebApp",
                              web_app=WebAppInfo(url=f"https://taldybayev.ru/values?values={values}"))],
        [InlineKeyboardButton(text="To Menu", callback_data="to_menu")]
    ])
    return inline_kb
