# Generated by Django 5.1.4 on 2024-12-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_rename_name_customuser_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='ip',
            new_name='IP',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('Session', 'Session'), ('Click', 'Click')], max_length=255),
        ),
    ]