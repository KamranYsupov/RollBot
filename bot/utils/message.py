from bot.keyboards.inline import get_inline_keyboard
from bot.loader import bot
from bot.models import Roll

async def send_roll_info(chat_id: int, roll: Roll):
    caption = (
        f'{roll.text}\n\n'
        f'<a href="{roll.link}">Ссылка</a>'
    )
    await bot.send_photo(
        chat_id=chat_id,
        photo='https://www.google.com/imgres?q=roll&imgurl=https%3A%2F%2Fcdn-img.perekrestok.ru%2Fi%2F800x800-fit%2Fxdelivery%2Ffiles%2F6d%2Fb8%2F14cf439c935948e2befbc0ca5cf4.jpg&imgrefurl=https%3A%2F%2Fwww.perekrestok.ru%2Fcat%2F298%2Fp%2Froll-sushi-roll-market-filadelfia-s-ogurcom-30g-4132619&docid=gAfoliGHMAB4FM&tbnid=rsLbHjXu0vOTwM&vet=12ahUKEwigvpvh5tGLAxV4IxAIHd_bFTQQM3oECHoQAA..i&w=800&h=800&hcb=2&ved=2ahUKEwigvpvh5tGLAxV4IxAIHd_bFTQQM3oECHoQAA',
        caption=caption,
        reply_markup=get_inline_keyboard(
            buttons={'Попробовать ещё раз': 'random_roll'}
        ),
        parse_mode='HTML',
    )
