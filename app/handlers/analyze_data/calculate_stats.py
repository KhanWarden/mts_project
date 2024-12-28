from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from app.database import AnalyzeCSV
from app.kbs import (max_columns_kb, MaxColumnsCallback, to_menu_kb, min_columns_kb, avg_columns_kb, MinColumnsCallback,
                     AverageColumnsCallback)
from app.states import TopStates

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "max_values")
async def calculate_stats_handler(call: CallbackQuery):
    await call.message.edit_text("Choose the column to see its max value",
                                 reply_markup=max_columns_kb())


@router.callback_query(MaxColumnsCallback.filter(F.name))
async def column_handler(call: CallbackQuery, callback_data: MaxColumnsCallback, state: FSMContext):
    column_name = callback_data.name
    column_name_normalized = column_name.replace("_", " ")
    await state.update_data(column_name=column_name,
                            column_name_normalized=column_name_normalized)

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
        await message.answer(f"<b>Max values from {column_name_normalized}:</b>\n"
                             f"{"\n".join(f"{i + 1}. {str(value)}" for i, value in enumerate(max_values))}",
                             reply_markup=to_menu_kb())
        await state.clear()
    except ValueError:
        await message.answer("It's not a number!")
    except Exception as e:
        await message.answer("Something went wrong.")
        print(e)


@router.callback_query(F.data == "min_values")
async def calculate_stats_handler(call: CallbackQuery):
    await call.message.edit_text("Choose the column to see its min value",
                                 reply_markup=min_columns_kb())


@router.callback_query(MinColumnsCallback.filter(F.name))
async def column_handler(call: CallbackQuery, callback_data: MinColumnsCallback, state: FSMContext):
    column_name = callback_data.name.replace("-", "_")
    column_name_normalized = column_name.replace("_", " ")
    await state.update_data(column_name=column_name,
                            column_name_normalized=column_name_normalized)

    await call.message.edit_text("Enter a number for «Top N Min Values»")
    await state.set_state(TopStates.min_n)


@router.message(TopStates.min_n)
async def min_n_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    column_name = data["column_name"]
    column_name_normalized = data["column_name_normalized"]

    try:
        n = int(message.text)
        max_values = analyze_csv.get_top_n_min_values(column_name, n)
        await message.answer(f"<b>Min values from {column_name_normalized}:</b>\n"
                             f"{"\n".join(f"{i + 1}. {str(value)}" for i, value in enumerate(max_values))}",
                             reply_markup=to_menu_kb())
        await state.clear()
    except ValueError:
        await message.answer("It's not a number!")
    except Exception as e:
        await message.answer("Something went wrong.")
        print(e)


@router.callback_query(F.data == "avg_values")
async def calculate_stats_handler(call: CallbackQuery):
    await call.message.edit_text("Choose the column to see its average value",
                                 reply_markup=avg_columns_kb())


@router.callback_query(AverageColumnsCallback.filter(F.name))
async def avg_column_handler(call: CallbackQuery, callback_data: AverageColumnsCallback):
    column_name = callback_data.name.replace(".", "_")
    column_name_normalized = column_name.replace("_", " ")
    avg_value = analyze_csv.get_average_value(column_name)
    await call.message.edit_text(f"<b>The average value from {column_name_normalized}:</b>\n"
                                 f"{avg_value}")
