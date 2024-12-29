from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.database import AnalyzeCSV
from app.kbs import columns_kb, ColumnsCallback, webapp_kb

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "correlation")
async def correlation_handler(call: CallbackQuery):
    await call.message.edit_text("Choose column 1",
                                 reply_markup=columns_kb("correlation_1"))


@router.callback_query(ColumnsCallback.filter(F.action == "correlation_1"))
async def column_handler(call: CallbackQuery, callback_data: ColumnsCallback, state: FSMContext):
    await state.update_data(column1=callback_data.column)
    await call.message.delete()
    await call.message.answer("Now, choose column 2",
                              reply_markup=columns_kb("correlation_2"))


@router.callback_query(ColumnsCallback.filter(F.action == "correlation_2"))
async def column_handler(call: CallbackQuery, callback_data: ColumnsCallback, state: FSMContext):
    data = await state.get_data()
    column1 = data["column1"]
    column2 = callback_data.column

    column1_fixed = column1.replace(" ", "_")
    column2_fixed = column2.replace(" ", "_")

    correlation = analyze_csv.calculate_correlation(column1_fixed, column2_fixed)
    await call.message.edit_text(f"Correlation between {column1} and {column2}:\n"
                                 f"{correlation}",
                                 reply_markup=webapp_kb(correlation))
    await state.clear()
