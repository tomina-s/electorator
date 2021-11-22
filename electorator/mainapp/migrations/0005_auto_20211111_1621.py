# Generated by Django 3.2.8 on 2021-11-11 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20211108_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 11, 11, 16, 21, 6, 967948), verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='birthday_place',
            field=models.CharField(blank=True, max_length=100, verbose_name='Место рождения'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='education',
            field=models.CharField(blank=True, max_length=200, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='polit_position',
            field=models.CharField(blank=True, max_length=200, verbose_name='Политическая дожность'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.CharField(blank=True, max_length=200, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='work',
            field=models.CharField(blank=True, max_length=200, verbose_name='Место работы'),
        ),
    ]