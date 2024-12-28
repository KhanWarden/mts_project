from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


def show_kb():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть данные по страницам", callback_data="show_pages")],
        [InlineKeyboardButton(text="Отправить Excel файл с данными", callback_data="send_excel")],
        [InlineKeyboardButton(text="Показать студента по ID", callback_data="show_stud_by_id")],
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="to_menu")]
    ])
    return inline_kb


def pagination_kb(current_page: int, total_pages: int):
    inline_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[])

    if current_page > 0:
        inline_kb.inline_keyboard.append([InlineKeyboardButton(text="⬅️ Назад",
                                                               callback_data=f"page_{current_page - 1}")])
    else:
        inline_kb.inline_keyboard.append([InlineKeyboardButton(text=" ", callback_data="None")])

    inline_kb.inline_keyboard.append([InlineKeyboardButton(text="В меню", callback_data="to_menu")])

    if current_page < total_pages - 1:
        inline_kb.inline_keyboard.append([InlineKeyboardButton(text="Вперед ➡️",
                                                               callback_data=f"page_{current_page + 1}")])
    else:
        inline_kb.inline_keyboard.append([InlineKeyboardButton(text=" ", callback_data="None")])

    inline_kb.inline_keyboard.append([InlineKeyboardButton(text="Открыть страницу в веб-приложении",
                                                           web_app=WebAppInfo(url="https://89c1-5-76-249-100.ngrok-free.app/page"))])

    return inline_kb
