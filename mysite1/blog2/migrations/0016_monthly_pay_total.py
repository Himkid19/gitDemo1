# Generated by Django 2.2.4 on 2019-10-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0015_auto_20191011_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_pay',
            name='total',
            field=models.CharField(default='0', max_length=30, verbose_name='总金额'),
        ),
    ]
