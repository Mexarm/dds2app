# Generated by Django 2.2 on 2019-04-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dds2app', '0002_auto_20190429_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sender',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sender',
            name='mobile_verified',
            field=models.BooleanField(default=False),
        ),
    ]
