from pathlib import Path
import pandas as pd
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile
from app.database import get_page, csv_to_excel
from app.kbs import pagination_kb, show_kb, main_kb
from app.methods import fix_path, csv_to_html

router = Router()
project_folder = Path(__file__).parent.parent.parent
csv_file = project_folder / 'data' / 'data.csv'
data = pd.read_csv(csv_file)
excel_file = project_folder / 'data' / 'data.xlsx'
html_file = project_folder / 'data' / 'data.html'


@router.callback_query(F.data == "None")
async def nothing(call: CallbackQuery):
    await call.answer()


@router.callback_query(F.data == "show_data")
async def show_data_handler(call: CallbackQuery):
    await call.message.edit_text("Выберите что сделать",
                                 reply_markup=show_kb())


@router.callback_query(F.data == "show_pages")
async def show_pages_handler(call: CallbackQuery):
    total_pages = (len(data) + 5 - 1) // 10
    page_data = get_page(0)
    await call.message.edit_text(f"Page 1 of {total_pages}\n\n"
                                 f"{page_data}",
                                 reply_markup=pagination_kb(0, total_pages))


@router.callback_query(F.data.startswith("page_"))
async def pagination_handler(call: CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[1])
    await state.update_data(page=page)
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
