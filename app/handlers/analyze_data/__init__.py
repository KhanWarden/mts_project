from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.kbs import analyze_data_kb
from .calculate_stats import router as calculate_stats_router
from .correlation import router as correlation_router
from .trends import router as trends_router
from .the_most_top import router as the_most_top_router

router = Router()
router.include_routers(calculate_stats_router,
                       correlation_router,
                       trends_router,
                       the_most_top_router)


@router.callback_query(F.data == "analyze_data")
async def analyze_data_handler(call: CallbackQuery):
    await call.message.edit_text("Выберите что сделать",
                                 reply_markup=analyze_data_kb())
