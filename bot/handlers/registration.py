import loguru
from aiogram import Router, types, F
from aiogram.enums import ChatMemberStatus
from aiogram.filters import CommandStart, Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext

from django.conf import settings

from bot.keyboards.reply import get_reply_contact_keyboard

router = Router()

@router.message(
    StateFilter('*'),
    F.text.lower() == 'отмена ❌'
)
async def cancel_handler(
        message: types.Message,
        state: FSMContext,
):
    await message.answer('Действие отменено')
    await state.clear()


@router.callback_query(F.data == 'check_subscription')
async def check_subscription_callback_handler(
        callback: types.CallbackQuery,
):
    chat_member = await callback.bot.get_chat_member(
        chat_id=settings.CHANNEL_ID,
        user_id=callback.from_user.id
    )
    member_statuses = (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.CREATOR
    )
    if chat_member.status not in member_statuses:
        await callback.answer("Ты не подписался ❌")
        return

    button_text = 'Отправить номер телефона 📲'
    await callback.message.delete()
    await callback.message.answer(
        'Для завершения регистрации'
        f'нажми на кнопу <b><em>"{button_text}"</em></b>, чтобы его отправить',
        reply_markup=get_reply_contact_keyboard(button_text),
        parse_mode='HTML',
    )

