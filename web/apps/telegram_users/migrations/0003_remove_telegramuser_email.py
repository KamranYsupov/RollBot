# Generated by Django 4.2.1 on 2025-03-04 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0002_telegramuser_date_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='email',
        ),
    ]
