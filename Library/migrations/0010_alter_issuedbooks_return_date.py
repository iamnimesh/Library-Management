# Generated by Django 4.1.3 on 2022-11-29 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0009_auto_20221129_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbooks',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 0, 2, 12, 482787)),
        ),
    ]