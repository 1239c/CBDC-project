# Generated by Django 3.2.16 on 2022-11-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0003_rename_coin_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='e_mail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
