# Generated by Django 5.1.4 on 2024-12-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_customuser_ip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_submission_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='submission_count',
            field=models.IntegerField(default=0),
        ),
    ]