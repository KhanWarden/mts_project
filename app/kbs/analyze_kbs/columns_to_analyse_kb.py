from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ColumnsCallback(CallbackData, prefix="columns"):
    action: str
    column: str


columns = ('Accuracy', 'Rhythm', 'Tempo', 'Pitch Accuracy', 'Duration', 'Volume', 'Heart Rate',
           'Blood Pressure', 'Focus Time', 'Performance Score', 'Engagement Score', 'Stress Level')


def columns_kb(action: str):
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=column,
                              callback_data=ColumnsCallback(action=action, column=column).pack())]
        for column in columns
    ])
    return inline_kb
