from django.db import models
from django.utils.translation import gettext_lazy as _

from web.db.model_mixins import (
    AsyncBaseModel,
)


class Roll(AsyncBaseModel):
    """Модель ролла"""
    image = models.ImageField(_('Картинка'), upload_to='images/')
    text = models.TextField(_('Текст'))
    link = models.URLField(_('Ссылка'))

    class Meta:
        verbose_name = _('Ролл')
        verbose_name_plural = _('Роллы')

    def __str__(self):
        return self.text[:50]

