# Generated by Django 2.2 on 2021-04-03 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210404_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default='Nil', max_length=30, verbose_name='name'),
        ),
    ]
