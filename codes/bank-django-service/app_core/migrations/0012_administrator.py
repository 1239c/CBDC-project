# Generated by Django 3.2.16 on 2022-11-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0011_auto_20221121_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('password_hash', models.CharField(max_length=100)),
            ],
        ),
    ]
