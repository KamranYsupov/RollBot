import random

from asgiref.sync import sync_to_async

from bot.models import Roll

@sync_to_async
def get_random_roll():
    # Генерируем случайный ID
    random_id =  random.choice(list(Roll.objects.values_list('id', flat=True)))

    return Roll.objects.get(id=random_id)