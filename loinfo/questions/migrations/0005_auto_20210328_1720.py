# Generated by Django 2.2 on 2021-03-28 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20210328_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 28, 17, 20, 3, 768431)),
        ),
    ]
