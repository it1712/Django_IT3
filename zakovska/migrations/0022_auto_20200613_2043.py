# Generated by Django 3.0.5 on 2020-06-13 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zakovska', '0021_auto_20200613_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='date',
            field=models.DateField(default=datetime.date.today, help_text='YYYY-MM-DD', verbose_name='Date'),
        ),
    ]
