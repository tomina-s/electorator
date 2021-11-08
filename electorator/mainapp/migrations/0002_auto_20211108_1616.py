# Generated by Django 3.2.8 on 2021-11-08 13:16

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
        migrations.AlterField(
            model_name='uik',
            name='num_tik',
            field=models.CharField(max_length=200, verbose_name='Номер ТИК'),
        ),
    ]
