# Generated by Django 3.2.8 on 2021-11-08 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211108_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tik',
            name='num_tik',
        ),
        migrations.RemoveField(
            model_name='uik',
            name='num_tik',
        ),
    ]
