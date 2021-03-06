# Generated by Django 2.1.4 on 2019-11-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0024_hydropower_last_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinfo',
            name='create_time',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='hydropower',
            name='create_time',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='last_time',
            field=models.DateField(auto_now=True, null=True, verbose_name='最近更新时间'),
        ),
        migrations.AlterField(
            model_name='hydropower',
            name='last_time',
            field=models.DateField(auto_now=True, null=True, verbose_name='最近更新时间'),
        ),
    ]
