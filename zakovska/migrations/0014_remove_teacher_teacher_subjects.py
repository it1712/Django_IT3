# Generated by Django 3.0.5 on 2020-05-25 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zakovska', '0013_teachersubject_ider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_subjects',
        ),
    ]
