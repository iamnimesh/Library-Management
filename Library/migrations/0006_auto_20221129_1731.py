# Generated by Django 3.1.5 on 2022-11-29 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_auto_20221128_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbooks',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 14, 17, 31, 11, 374344)),
        ),
    ]
