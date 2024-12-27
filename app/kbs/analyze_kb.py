from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def analyze_data_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посчитать статистику", callback_data="calculate_stats")],
        [InlineKeyboardButton(text="Фильтровать данные", callback_data="filter_data")],
        [InlineKeyboardButton(text="Добавить запись", callback_data="add_new_row")],
        [InlineKeyboardButton(text="Изменить запись", callback_data="change_row")],
        [InlineKeyboardButton(text="Удалить запись", callback_data="delete_row")],
    ])
    return inline_kb
