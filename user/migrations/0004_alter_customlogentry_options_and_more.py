# Generated by Django 4.2.7 on 2023-11-30 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_options_alter_customuser_table_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customlogentry',
            options={'verbose_name': 'customlogentry', 'verbose_name_plural': 'customlogentries'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'customuser', 'verbose_name_plural': 'customusers'},
        ),
        migrations.AlterModelTable(
            name='customlogentry',
            table='customlogentry',
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='customuser',
        ),
    ]
