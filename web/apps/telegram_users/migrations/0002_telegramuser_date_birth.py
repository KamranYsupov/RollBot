# Generated by Django 4.2.1 on 2025-02-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='date_birth',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата рождения'),
        ),
    ]
