from pathlib import Path
import pandas as pd
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, Message
from app.database import get_page, csv_to_excel, CSVParser
from app.kbs import pagination_kb, show_kb, main_kb, to_menu_kb
from app.methods import fix_path, csv_to_html, format_id
from app.states import ShowDataStates

router = Router()
project_folder = Path(__file__).parent.parent.parent
csv_file = project_folder / 'data' / 'data.csv'
data = pd.read_csv(csv_file)
excel_file = project_folder / 'data' / 'data.xlsx'
html_file = project_folder / 'data' / 'data.html'
csv_parser = CSVParser()


@router.callback_query(F.data == "None")
async def nothing(call: CallbackQuery):
    await call.answer()


@router.callback_query(F.data == "show_data")
async def show_data_handler(call: CallbackQuery):
    await call.message.edit_text("Выберите что сделать",
                                 reply_markup=show_kb())


@router.callback_query(F.data == "show_pages")
async def show_pages_handler(call: CallbackQuery, state: FSMContext):
    total_pages = (len(data) + 5 - 1) // 10
    page_data = get_page(0)
    await csv_to_html(0)
    await call.message.edit_text(f"Page 1 of {total_pages}\n\n"
                                 f"{page_data}",
                                 reply_markup=pagination_kb(0, total_pages))


@router.callback_query(F.data.startswith("page_"))
async def pagination_handler(call: CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[1])
    await csv_to_html(int(page))
    total_pages = (len(data) + 5 - 1) // 10
    page_data = get_page(page)
    await call.message.edit_text(f"Page {page + 1} of {total_pages}\n\n"
                                 f"{page_data}",
                                 reply_markup=pagination_kb(page, total_pages))


@router.callback_query(F.data == "export_page")
async def export_page_to_html_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    state_data = await state.get_data()
    page = int(state_data["page"])

    await csv_to_html(page)
    await call.message.answer_document(FSInputFile(str(html_file)))


@router.callback_query(F.data == "send_excel")
async def send_excel_handler(call: CallbackQuery):
    await call.message.delete()
    await csv_to_excel()
    await call.message.answer_document(FSInputFile(str(excel_file)))
    await call.message.answer("I am a bot for Python Project\n"
                              "My creators are:\n"
                              "<b>1. Taldybayev Batyrkhan</b>\n"
                              "<b>2. Murdasov Alexander</b>\n"
                              "<b>3. Sulimenov Zhaslan</b>",
                              reply_markup=main_kb())


@router.callback_query(F.data == "show_stud_by_id")
async def show_student_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Впишите ID студента")
    await state.set_state(ShowDataStates.stud_id)


@router.message(ShowDataStates.stud_id)
async def show_student_handler(message: Message, state: FSMContext):
    try:
        stud_id = int(message.text)
        stud_id = format_id(stud_id)
        await message.answer(csv_parser.get_formatted_row(student_id=stud_id),
                             reply_markup=to_menu_kb())
        await state.clear()

    except Exception as e:
        print(e)
        await message.answer("Неверное число!")
