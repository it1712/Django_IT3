# Generated by Django 3.0.5 on 2020-05-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zakovska', '0012_auto_20200525_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachersubject',
            name='ider',
            field=models.IntegerField(null=True, verbose_name='id'),
        ),
    ]