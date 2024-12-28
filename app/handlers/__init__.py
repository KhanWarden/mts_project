from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.kbs import main_kb
from .show_data_handlers import router as show_data_router
from .analyze_data import router as analyze_data_router

router = Router()
router.include_routers(show_data_router, analyze_data_router)


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("I am a bot for Python Project\n"
                         "My creators are:\n"
                         "<b>1. Taldybayev Batyrkhan</b>\n"
                         "<b>2. Murdasov Alexander</b>\n"
                         "<b>3. Sulimenov Zhaslan</b>",
                         reply_markup=main_kb())


@router.callback_query(F.data == "to_menu")
async def to_menu_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("I am a bot for Python Project\n"
                                 "My creators are:\n"
                                 "<b>1. Taldybayev Batyrkhan</b>\n"
                                 "<b>2. Murdasov Alexander</b>\n"
                                 "<b>3. Sulimenov Zhaslan</b>",
                                 reply_markup=main_kb())
