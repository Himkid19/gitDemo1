# Generated by Django 2.2.4 on 2019-09-30 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0011_monthly_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_pay',
            name='house_no',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog2.HouseInfo'),
        ),
    ]
