# Generated by Django 4.2.19 on 2025-03-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0013_programinfo_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='programinfo',
            name='program_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='programinfo',
            name='added_date',
            field=models.DateField(auto_now=True),
        ),
    ]
