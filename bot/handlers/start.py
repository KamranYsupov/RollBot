import loguru
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from django.conf import settings

from bot.keyboards.inline import get_inline_keyboard
from bot.models import TelegramUser

router = Router()


@router.message(CommandStart())
async def start_command_handler(
    message: types.Message,
):
    message_text = f'Привет, {message.from_user.first_name} 👋. '
    reply_markup = None

    telegram_user = await TelegramUser.objects.aget(telegram_id=message.from_user.id)

    if not telegram_user:
        message_text += \
            f'Для старта работы бота <a href={settings.CHANNEL_LINK}>подпишись на канал</b> 👇'
        reply_markup = get_inline_keyboard(
            buttons={'Я подписан(а) ✅': 'check_subscription'}
        )

    await message.answer(
        message_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )
    
    
    

    
    

