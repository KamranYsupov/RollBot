from django.contrib import admin

from .models import Roll


@admin.register(Roll)
class RollAdmin(admin.ModelAdmin):
    pass
