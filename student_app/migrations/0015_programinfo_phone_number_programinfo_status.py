# Generated by Django 4.2.19 on 2025-03-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0014_programinfo_program_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='programinfo',
            name='phone_number',
            field=models.CharField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='programinfo',
            name='status',
            field=models.CharField(default='ready', max_length=20),
        ),
    ]
