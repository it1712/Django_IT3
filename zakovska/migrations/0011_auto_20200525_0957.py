# Generated by Django 3.0.5 on 2020-05-25 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zakovska', '0010_teachersubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakovska.TeacherSubject'),
        ),
    ]