from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.database import CSVParser

csv_parser = CSVParser()


class CallbackForAnalysis(CallbackData, prefix="callback"):
    instrument: str | None = None
    class_level: str | None = None


def instruments_kb():
    instruments = csv_parser.get_unique_column_values("Instrument_Type")
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=instrument, callback_data=CallbackForAnalysis(instrument=instrument).pack())]
        for instrument in instruments
    ])
    inline_kb.inline_keyboard.append([InlineKeyboardButton(text="В меню", callback_data="to_menu")])
    return inline_kb


def class_levels_kb():
    class_levels = csv_parser.get_unique_column_values("Class_Level")
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=class_level, callback_data=CallbackForAnalysis(class_level=class_level).pack())]
        for class_level in class_levels
    ])
    inline_kb.inline_keyboard.append([InlineKeyboardButton(text="В меню", callback_data="to_menu")])
    return inline_kb
