from typing import Union

from aiogram import F, types, Router
from aiogram.filters import Command

from bot.orm.roll import get_random_roll
from bot.utils.message import send_roll_info
from bot.models import TelegramUser

router = Router()

@router.callback_query(F.data == 'random_roll')
@router.message(Command('random_roll'))
async def random_roll_handler(aiogram_type: Union[types.CallbackQuery | types.Message]):
    if isinstance(aiogram_type, types.Message):
        message = aiogram_type
        telegram_user = await TelegramUser.objects.aget(telegram_id=message.from_user.id)
        if not telegram_user:
            await message.answer('Сначала пройдите регистрацию')
            return

    roll = await get_random_roll()
    await send_roll_info(chat_id=aiogram_type.from_user.id, roll=roll)