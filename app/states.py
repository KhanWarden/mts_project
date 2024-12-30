from aiogram.fsm.state import StatesGroup, State


class ShowDataStates(StatesGroup):
    stud_id = State()


class TopStates(StatesGroup):
    max_n = State()
    min_n = State()


class Analyze(StatesGroup):
    stud_id = State()
