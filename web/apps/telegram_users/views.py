from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.conf import settings

from .service import export_telegram_users_to_excel


@staff_member_required
@require_http_methods(["GET"])
def export_telegram_users_to_excel_view(request):
    """
    View для экспорта Telegram пользователей в Excel.
    """
    excel_data = export_telegram_users_to_excel()

    response = HttpResponse(
        excel_data,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = \
        f'attachment; filename="{settings.DEFAULT_TELEGRAM_USERS_EXCEL_DATA_FILENAME}"'

    return response
