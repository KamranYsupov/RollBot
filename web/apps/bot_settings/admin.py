from django.contrib import admin

from .models import BotSettings
from web.admin.mixins import SingletonModelAdminMixin


@admin.register(BotSettings)
class BotSettingsAdmin(SingletonModelAdminMixin):
    pass
