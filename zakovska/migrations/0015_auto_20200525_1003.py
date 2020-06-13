# Generated by Django 3.0.5 on 2020-05-25 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zakovska', '0014_remove_teacher_teacher_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_subjects',
            field=models.ManyToManyField(help_text="Select teacher's subjects", to='zakovska.Subject'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakovska.Subject'),
        ),
        migrations.DeleteModel(
            name='TeacherSubject',
        ),
    ]