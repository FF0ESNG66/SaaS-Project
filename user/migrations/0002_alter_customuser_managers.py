# Generated by Django 4.2.7 on 2023-11-30 18:24

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', user.managers.CustomUserManager()),
            ],
        ),
    ]
