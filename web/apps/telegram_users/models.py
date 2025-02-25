from django.db import models
from django.utils.translation import gettext_lazy as _

from web.db.model_mixins import (
    AbstractTelegramUser,
)


class TelegramUser(AbstractTelegramUser):
    """Модель telegram пользователя"""
    fio = models.CharField(
        _('ФИО'),
        max_length=150
    )
    phone_number = models.CharField(
        _('Номер телефона'),
        max_length=50,
        unique=True,
    )
    email = models.EmailField(
        _('E-mail'),
        unique=True,
    )
    date_birth = models.DateField(
        _('Дата рождения'),
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('Telegram пользователи')

    def __str__(self):
        return f'{self.fio} {self.phone_number}'
