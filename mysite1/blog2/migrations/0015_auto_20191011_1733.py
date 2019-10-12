# Generated by Django 2.2.4 on 2019-10-11 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0014_auto_20191006_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthly_pay',
            name='user',
        ),
        migrations.AddField(
            model_name='monthly_pay',
            name='create_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthly_pay',
            name='last_time',
            field=models.DateField(auto_now=True, verbose_name='最后修改时间'),
        ),
    ]