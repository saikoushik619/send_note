# Generated by Django 4.2.19 on 2025-03-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0008_programinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programinfo',
            name='program_message',
            field=models.CharField(max_length=210),
        ),
    ]
