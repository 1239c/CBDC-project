# Generated by Django 3.2.16 on 2022-10-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
    ]
