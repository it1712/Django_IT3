# Generated by Django 3.0.5 on 2020-06-13 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zakovska', '0015_auto_20200525_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_subjects',
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakovska.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakovska.Teacher')),
            ],
        ),
        migrations.AlterField(
            model_name='mark',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakovska.TeacherSubject'),
        ),
    ]