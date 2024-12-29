from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.database import AnalyzeCSV
from app.kbs import webapp_kb

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "best_student")
async def best_student(call: CallbackQuery):
    the_best_student = analyze_csv.best_student()
    await call.message.edit_text(f"The best student:\n"
                                 f"{the_best_student}",
                                 reply_markup=webapp_kb(the_best_student))


@router.callback_query(F.data == "engaged_student")
async def engaged_student(call: CallbackQuery):
    the_most_engaged_student = analyze_csv.most_engaged_student()
    await call.message.edit_text(f"The most engaged student:\n"
                                 f"{the_most_engaged_student}",
                                 reply_markup=webapp_kb(the_most_engaged_student))


@router.callback_query(F.data == "difficult_lesson")
async def difficult_lesson(call: CallbackQuery):
    the_most_difficult_lesson = analyze_csv.most_difficult_lesson()
    await call.message.edit_text(f"The most difficult lesson:\n"
                                 f"{the_most_difficult_lesson}",
                                 reply_markup=webapp_kb(the_most_difficult_lesson))
