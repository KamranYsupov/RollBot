from asgiref.sync import sync_to_async
from django.conf import settings
from aiogram.types import FSInputFile
from bot.keyboards.inline import get_inline_keyboard
from bot.loader import bot
from bot.models import Roll
from web.apps.bot_settings.models import BotSettings


async def send_roll_info(chat_id: int, roll: Roll):
    caption = (
        f'{roll.text}\n\n'
        f'<a href="{roll.link}">Попробуй свой ролл на вкус🍣</a>'
    )
    photo = FSInputFile(f'web/media/{roll.image.name}')

    bot_settings: BotSettings = await sync_to_async(BotSettings.load)()
    await bot.send_photo(
        chat_id=chat_id,
        photo=photo,
        caption=caption,
        reply_markup=get_inline_keyboard(
            buttons={bot_settings.roll_buttons_text: 'random_roll'}
        ),
        parse_mode='HTML',
    )
