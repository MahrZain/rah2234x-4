# Generated by Django 5.1.4 on 2024-12-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_customuser_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='IP',
            field=models.GenericIPAddressField(unpack_ipv4=True),
        ),
    ]
