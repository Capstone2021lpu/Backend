# Generated by Django 2.2 on 2021-04-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20210403_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
