# Generated by Django 5.1.4 on 2024-12-12 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_alter_customuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_submission_time',
        ),
    ]
