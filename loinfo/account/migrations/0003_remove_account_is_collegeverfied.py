# Generated by Django 2.2 on 2021-04-03 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_is_collegeverfied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_collegeverfied',
        ),
    ]
