from django.db import models
from django.utils.translation import gettext_lazy as _

from web.db.model_mixins import (
    AsyncBaseModel, SingletonModelMixin,
)


class BotSettings(AsyncBaseModel, SingletonModelMixin):
    """Модель текстов бота"""
    text_after_registration = models.TextField(
        _('Текст после регистрации'),
        max_length=4000,
    )
    roll_buttons_text = models.TextField(_('Текст кнопки под роллом'),)

    class Meta:
        verbose_name = _('Тексты бота')
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Тексты бота'
