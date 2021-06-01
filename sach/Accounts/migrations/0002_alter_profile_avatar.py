# Generated by Django 3.2.3 on 2021-06-01 13:23

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='users/avatar.png', upload_to=Accounts.models.user_directory_path),
        ),
    ]