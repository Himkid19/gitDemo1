# Generated by Django 2.1.4 on 2019-11-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0025_auto_20191128_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseinfo',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='hydropower',
            name='create_time',
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='last_time',
            field=models.DateField(auto_now=True, verbose_name='最近更新时间'),
        ),
        migrations.AlterField(
            model_name='hydropower',
            name='last_time',
            field=models.DateField(auto_now=True, verbose_name='最近更新时间'),
        ),
    ]
