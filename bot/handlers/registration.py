from datetime import datetime
import random

import loguru
from aiogram import Router, types, F
from aiogram.enums import ChatMemberStatus
from aiogram.filters import CommandStart, Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from bot.keyboards.reply import get_reply_contact_keyboard, reply_keyboard_remove, reply_cancel_keyboard
from bot.orm.roll import get_random_roll
from bot.states.telegram_user import TelegramUserState
from bot.models import TelegramUser, Roll
from bot.utils.message import send_roll_info

router = Router()


@router.message(
    StateFilter('*'),
    F.text.lower() == 'отмена ❌'
)
async def cancel_handler(
        message: types.Message,
        state: FSMContext,
):
    await message.answer(
        'Действие отменено',
        reply_markup=reply_keyboard_remove,
    )
    await state.clear()


@router.callback_query(F.data == 'check_subscription')
async def check_subscription_callback_handler(
        callback: types.CallbackQuery,
        state: FSMContext
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
        await callback.answer("Вы не подписались ❌")
        return

    button_text = 'Отправить номер телефона 📲'
    await callback.message.delete()
    await callback.message.answer(
        'Для регистрации '
        f'нажмите на кнопу <b><em>"{button_text}"</em></b>, чтобы его отправить',
        reply_markup=get_reply_contact_keyboard(button_text),
        parse_mode='HTML',
    )

    await state.set_state(TelegramUserState.phone_number)


@router.message(StateFilter(TelegramUserState.phone_number), F.contact)
async def process_phone_number_message_handler(
        message: types.Message,
        state: FSMContext
):
    await state.update_data(phone_number=message.contact.phone_number)

    await message.answer(
        'Укажите ваше ФИО',
        reply_markup=reply_cancel_keyboard,
    )
    await state.set_state(TelegramUserState.fio)


@router.message(StateFilter(TelegramUserState.fio), F.text)
async def process_fio_message_handler(
        message: types.Message,
        state: FSMContext
):
    await state.update_data(fio=message.text)

    await message.answer(
        'Отправьте дату рождения в формате: <b>День.Месяц.Год</b>.\n'
        '<b>Пример: <em>01.11.2004</em></b>',
        parse_mode='HTML'
    )
    await state.set_state(TelegramUserState.date_birth)


@router.message(StateFilter(TelegramUserState.date_birth), F.text)
async def process_date_birth_message_handler(
        message: types.Message,
        state: FSMContext
):
    loguru.logger.info('dsaddsad')
    try:
        date_birth = datetime.strptime(message.text, "%d.%m.%Y").date()
    except ValueError:
        await message.answer(
            'Некорректная дата рождения\n\n'
            'Пример: <b>01.11.2004</b>',
            parse_mode='HTML'
        )
        return

    await state.update_data(date_birth=date_birth)

    await message.answer('Укажите почту')
    await state.set_state(TelegramUserState.email)


@router.message(StateFilter(TelegramUserState.email), F.text)
async def process_email_message_handler(
        message: types.Message,
        state: FSMContext
):
    email = message.text
    try:
        validate_email(email)
    except ValidationError:
        await message.answer('Некорректный E-mail')
        return

    await state.update_data(telegram_id=message.from_user.id)
    await state.update_data(username=message.from_user.username)
    await state.update_data(email=email)

    state_data = await state.get_data()
    await TelegramUser.objects.acreate(**state_data)
    await state.clear()

    await message.answer(
        'Регистрация успешно завершена!',
        reply_markup=reply_keyboard_remove,
    )
    roll = await get_random_roll()
    await send_roll_info(
        chat_id=message.from_user.id,
        roll=roll,
    )








