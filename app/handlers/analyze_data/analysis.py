from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from app.database import AnalyzeCSV
from app.kbs import instruments_kb, CallbackForAnalysis, class_levels_kb, webapp_kb

router = Router()
analyze_csv = AnalyzeCSV()


@router.callback_query(F.data == "average_perf_score")
async def average_performance_score_handler(call: CallbackQuery):
    await call.message.edit_text(f"Average performance score according to instrument and class level\n"
                                 f"Choose the Instrument",
                                 reply_markup=instruments_kb())


@router.callback_query(CallbackForAnalysis.filter(F.instrument))
async def instrument_handler(call: CallbackQuery, callback_data: CallbackForAnalysis, state: FSMContext):
    await state.update_data(instrument=callback_data.instrument)
    await call.message.edit_text("Now, choose class level",
                                 reply_markup=class_levels_kb())


@router.callback_query(CallbackForAnalysis.filter(F.class_level))
async def class_level_handler(call: CallbackQuery, callback_data: CallbackForAnalysis, state: FSMContext):
    data = await state.get_data()
    instrument = data["instrument"]
    class_level = callback_data.class_level

    avg_score = analyze_csv.average_performance_score(instrument, class_level)
    await call.message.edit_text(f"Average performance score according to {instrument} and {class_level} is:\n"
                                 f"{avg_score}",
                                 reply_markup=webapp_kb(avg_score))


"""################################################################################"""


@router.callback_query(F.data == "correlation_between_two")
async def correlation_between_two_handler(call: CallbackQuery):
    correlation = analyze_csv.engagement_impact_on_skill_development()
    await call.message.edit_text(f"Correlation between Engagement Level and Skill Development: {correlation:.2f}",
                                 reply_markup=webapp_kb(correlation))
