from django.conf import settings

from bot.keyboards.inline import get_inline_keyboard
from bot.loader import bot
from bot.models import Roll

async def send_roll_info(chat_id: int, roll: Roll):
    caption = (
        f'{roll.text}\n\n'
        f'<a href="{roll.link}">Ссылка</a>'
    )

    photo_url = f'{settings.BASE_URL}{roll.image.url}'
    await bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=get_inline_keyboard(
            buttons={'Попробовать ещё раз': 'random_roll'}
        ),
        parse_mode='HTML',
    )
