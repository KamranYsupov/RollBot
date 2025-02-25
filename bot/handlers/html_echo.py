import loguru
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from bot.models import TelegramUser


class FormatedTextState(StatesGroup):
    text = State()

router = Router()

@router.message(Command('html_echo'))
async def html_echo_command_handler(
    message: types.Message,
    state: FSMContext,
):
    await state.set_state(FormatedTextState.text)
    await message.answer('Отправьте текст.')


@router.message(F.text, FormatedTextState.text)
async def formated_html_text_handler(
    message: types.Message,
    state: FSMContext,
):
    await message.answer(message.html_text)
    await state.clear()