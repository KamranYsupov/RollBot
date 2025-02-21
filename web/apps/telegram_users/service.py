from typing import Optional

import pandas as pd
from io import BytesIO
from django.db import transaction

from .models import TelegramUser


def export_telegram_users_to_excel(file_name=None) -> Optional[bytes]:
    """
    Экспортирует telegram пользоветелей в Excel.

    :param file_name: Если указан, сохраняет файл на сервере. Если None, возвращает бинарные данные.
    :return: Если file_name=None, возвращает бинарные данные (bytes). Иначе возвращает None.
    """
    data = []

    telegram_users = TelegramUser.objects.all()

    for telegram_user in telegram_users:
        telegram_user_data = {
            'ID': telegram_user.id,
            'Телеграм ID': telegram_user.telegram_id,
            'Имя пользователя': telegram_user.username,
            'ФИО': telegram_user.fio,
            'Номер телефона': telegram_user.phone_number,
            'E-mail': telegram_user.email,
        }
        data.append(telegram_user_data)

    df = pd.DataFrame(data)

    if file_name:
        df.to_excel(file_name, index=False)
        return None

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    excel_data = output.getvalue()
    return excel_data
