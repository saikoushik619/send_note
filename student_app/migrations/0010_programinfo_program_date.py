# Generated by Django 4.2.19 on 2025-03-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0009_alter_programinfo_program_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='programinfo',
            name='program_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
