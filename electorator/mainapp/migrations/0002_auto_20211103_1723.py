# Generated by Django 3.2.8 on 2021-11-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tik',
            name='open_uik',
            field=models.IntegerField(default=0, verbose_name='Число открытых участков'),
        ),
        migrations.AlterField(
            model_name='tik',
            name='population',
            field=models.IntegerField(default=0, verbose_name='Численность'),
        ),
    ]