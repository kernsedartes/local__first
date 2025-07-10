from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
import logging
from datetime import datetime
from django.conf import settings
from .forms import DealForm

logger = logging.getLogger(__name__)

# Домашняя страница
@main_auth(on_cookies=True, set_cookie=True)
def home(request):
    try:
        app_settings = settings.APP_SETTINGS
        user_info = request.bitrix_user_token.call_api_method('user.current')
        user_name = f"{user_info['result']['NAME']} {user_info['result']['LAST_NAME']}"
    except Exception as e:
        logger.error(f"Ошибка получения текущего пользователя: {e}")
        user_name = "Unknown User"

    return render(request, 'bitrixapp/home.html', locals())


# Страница со списком сделок
@main_auth(on_cookies=True)
def deals(request):
    but = request.bitrix_user_token

    try:
        user_info = but.call_api_method('user.current')
        user_name = f"{user_info['result']['NAME']} {user_info['result']['LAST_NAME']}"

        # Получаем все поля сделки (удалили параметр 'select')
        deals = but.call_api_method('crm.deal.list', {
            'filter': {'CLOSED': 'N'},
            'order': {'DATE_MODIFY': 'DESC'},
            'select': [
                'ID', 'TITLE', 'STAGE_ID', 'OPPORTUNITY', 'CURRENCY_ID',
                'BEGINDATE', 'CLOSEDATE', 'UF_CRM_1752098496'
            ],
            'start': 0,
            'limit': 10
        }).get('result', [])[:10]

    except Exception as e:
        user_name = "Unknown User"
        deals = []

    return render(request, 'bitrixapp/deals.html', locals())


# Создание сделки
@main_auth(on_cookies=True)
def create_deal(request):
    but = request.bitrix_user_token

    try:
        user_info = but.call_api_method('user.current')
        user_name = f"{user_info['result']['NAME']} {user_info['result']['LAST_NAME']}"
    except Exception as e:
        logger.error(f"Ошибка получения текущего пользователя: {e}")
        user_name = "Unknown User"

    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            try:
                but.call_api_method('crm.deal.add', {
                    'fields': {
                        'TITLE': form.cleaned_data['title'],
                        'STAGE_ID': form.cleaned_data['stage_id'],
                        'CURRENCY_ID': form.cleaned_data['currency'],
                        'OPPORTUNITY': float(form.cleaned_data['price']),
                        'BEGINDATE': form.cleaned_data['begindate'].strftime('%Y-%m-%d'),
                        'CLOSEDATE': form.cleaned_data['closedate'].strftime('%Y-%m-%d'),
                        'UF_CRM_1752098496': form.cleaned_data['custom_field'],
                    }
                })
                return redirect('deals')
            except Exception as e:
                logger.error(f"Ошибка создания сделки: {e}")
    else:
        form = DealForm()

    return render(request, 'bitrixapp/create_deal.html', locals())