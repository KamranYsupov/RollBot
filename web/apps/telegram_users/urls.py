from django.urls import path
from . import views

urlpatterns = [
    path(
        'export-telegram-users-to-excel/',
        views.export_telegram_users_to_excel_view,
        name='export_telegram_users_to_excel'
    ),
]
