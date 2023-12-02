# Generated by Django 4.2.7 on 2023-11-30 19:37

from django.conf import settings
import django.contrib.admin.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('user', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'CustomUser', 'verbose_name_plural': 'CustomUsers'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='CustomUser',
        ),
        migrations.CreateModel(
            name='CustomLogEntry',
            fields=[
                ('logentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='admin.logentry')),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CustomLogEntry',
                'verbose_name_plural': 'CustomLogEntries',
                'db_table': 'CustomLogEntry',
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]