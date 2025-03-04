from aiogram.fsm.state import StatesGroup, State


class TelegramUserState(StatesGroup):
    telegram_id = State()
    username = State()
    phone_number = State()
    fio = State()
    date_birth = State()
