from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiohttp import ClientSession
from app.database import AnalyzeCSV
from app.kbs import (ColumnsCallback, webapp_kb, columns_kb)
from app.states import TopStates

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "max_values")
async def calculate_stats_handler(call: CallbackQuery):
    await call.message.edit_text("Choose the column to see its max value",
                                 reply_markup=columns_kb(action="max_values_call"))


@router.callback_query(ColumnsCallback.filter(F.action == "max_values_call"))
async def column_handler(call: CallbackQuery, callback_data: ColumnsCallback, state: FSMContext):
    column_name = callback_data.column
    column_name_fixed = column_name.replace(" ", "_")
    await state.update_data(column_name=column_name_fixed,
                            column_name_normalized=column_name)

    await call.message.edit_text("Enter a number for «Top N Max Values»")
    await state.set_state(TopStates.max_n)


@router.message(TopStates.max_n)
async def max_n_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    column_name = data["column_name"]
    column_name_normalized = data["column_name_normalized"]

    try:
        n = int(message.text)
        max_values = analyze_csv.get_top_n_max_values(column_name, n)
        values = ",".join(map(str, max_values))
        await message.answer(f"<b>Max values from {column_name_normalized}:</b>\n"
                             f"{"\n".join(f"{i + 1}. {str(value)}" for i, value in enumerate(max_values))}",
                             reply_markup=webapp_kb(values))
        await state.clear()
    except ValueError:
        await message.answer("It's not a number!")
    except Exception as e:
        await message.answer("Something went wrong.")
        print(e)


@router.callback_query(F.data == "min_values")
async def calculate_stats_handler(call: CallbackQuery):
    await call.message.edit_text("Choose the column to see its min value",
                                 reply_markup=columns_kb(action="min_values_call"))


@router.callback_query(ColumnsCallback.filter(F.action == "min_values_call"))
async def column_handler(call: CallbackQuery, callback_data: ColumnsCallback, state: FSMContext):
    column_name = callback_data.column
    column_name_fixed = column_name.replace(" ", "_")
    await state.update_data(column_name=column_name_fixed,
                            column_name_normalized=column_name)

    await call.message.edit_text("Enter a number for «Top N Min Values»")
    await state.set_state(TopStates.min_n)


@router.message(TopStates.min_n)
async def min_n_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    column_name = data["column_name"]
    column_name_normalized = data["column_name_normalized"]

    try:
        n = int(message.text)
        min_values = list(analyze_csv.get_top_n_min_values(column_name, n))
        values = ",".join(map(str, min_values))
        await message.answer(f"<b>Min values from {column_name_normalized}:</b>\n"
                             f"{"\n".join(f"{i + 1}. {str(value)}" for i, value in enumerate(min_values))}",
                             reply_markup=webapp_kb(values))
        await state.clear()
    except ValueError:
        await message.answer("It's not a number!")
    except Exception as e:
        await message.answer("Something went wrong.")
        print(e)


@router.callback_query(F.data == "avg_values")
async def calculate_stats_handler(call: CallbackQuery):
    await call.message.edit_text("Choose the column to see its average value",
                                 reply_markup=columns_kb(action="average_values_call"))


@router.callback_query(ColumnsCallback.filter(F.action == "avg_values_call"))
async def avg_column_handler(call: CallbackQuery, callback_data: ColumnsCallback):
    column_name = callback_data.column
    column_name_fixed = column_name.replace(" ", "_")
    avg_value = analyze_csv.get_average_value(column_name)
    await call.message.edit_text(f"<b>The average value from {column_name}:</b>\n"
                                 f"{avg_value}",
                                 reply_markup=webapp_kb(avg_value))
