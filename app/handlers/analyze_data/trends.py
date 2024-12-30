from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from app.database import AnalyzeCSV
from app.kbs import webapp_kb, productivity_kb
from app.methods import format_id
from app.states import Analyze

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "productivity")
async def prod_handler(call: CallbackQuery):
    await call.message.edit_text("Выберите что нужно",
                                 reply_markup=productivity_kb())


@router.callback_query(F.data == "productivity_all")
async def prod_handler(call: CallbackQuery):
    data_dict = analyze_csv.calculate_productivity()
    avg_performance_score = data_dict["average_performance_score"]
    avg_stress_level = data_dict["average_stress_level"]
    productivity = data_dict["productivity_coefficient"]

    await call.message.edit_text(f"<b>Performance Score / Stress Level = Productivity</b>\n"
                                 f"{avg_stress_level} / {avg_performance_score} = {productivity}",
                                 reply_markup=webapp_kb(productivity))


@router.callback_query(F.data == "productivity_of_student")
async def prod_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите ID студента")
    await state.set_state(Analyze.stud_id)


@router.message(Analyze.stud_id)
async def stud_id_handler(message: Message, state: FSMContext):
    try:
        stud_id = format_id(int(message.text))
        data_dict = analyze_csv.calculate_productivity_of_student(stud_id)
        performance_score = data_dict["performance_score"]
        stress_level = data_dict["stress_level"]
        productivity = data_dict["productivity_coefficient"]

        await message.answer(f"<b>Performance Score / Stress Level = Productivity</b>\n"
                             f"{stress_level} / {performance_score} = {productivity}",
                             reply_markup=webapp_kb(productivity))
        await state.clear()
    except ValueError:
        await message.answer("Неверное ID!")
