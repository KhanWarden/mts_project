from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.database import AnalyzeCSV
from app.kbs import webapp_kb

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "productivity")
async def trends_handler(call: CallbackQuery):
    data_dict = analyze_csv.calculate_productivity()
    avg_performance_score = data_dict["average_performance_score"]
    avg_stress_level = data_dict["average_stress_level"]
    productivity = data_dict["productivity_coefficient"]

    await call.message.edit_text(f"<b>Performance Score / Stress Level = Productivity</b>\n"
                                 f"{avg_performance_score} / {avg_stress_level} = {productivity}",
                                 reply_markup=webapp_kb(productivity))
