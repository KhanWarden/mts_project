from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router = Router()
router.include_routers()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("I am a bot for Python Project\n"
                         "My creators are:\n"
                         "<b>1. Taldybayev Batyrkhan</b>\n"
                         "<b>2. Murdasov Alexander</b>\n"
                         "<b>3. Sulimenov Zhaslan</b>")
