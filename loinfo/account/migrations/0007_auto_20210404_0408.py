# Generated by Django 2.2 on 2021-04-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default='Guest', max_length=30, verbose_name='name'),
        ),
    ]
