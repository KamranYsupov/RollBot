# Generated by Django 4.2.1 on 2025-02-19 18:00

from django.db import migrations, models
import web.db.model_mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.CharField(db_index=True, default=web.db.model_mixins.ulid_default, editable=False, max_length=26, primary_key=True, serialize=False, unique=True)),
                ('telegram_id', models.BigIntegerField(db_index=True, unique=True, verbose_name='Телеграм ID')),
                ('username', models.CharField(db_index=True, max_length=70, null=True, unique=True, verbose_name='Имя пользователя')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=50, unique=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'Telegram пользователи',
            },
        ),
    ]
