# Generated by Django 2.1.4 on 2019-12-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0033_auto_20191206_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='session_key',
            field=models.CharField(blank=True, max_length=64, verbose_name='session_key'),
        ),
    ]