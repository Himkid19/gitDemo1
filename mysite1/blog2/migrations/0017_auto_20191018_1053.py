# Generated by Django 2.2.4 on 2019-10-18 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0016_monthly_pay_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_pay',
            name='house_no',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog2.HouseInfo', to_field='house_no', unique=True),
        ),
    ]
