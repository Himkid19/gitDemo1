# Generated by Django 2.2.4 on 2019-09-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0002_house_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_info',
            name='status',
            field=models.CharField(choices=[('0', '闲置'), ('1', '已售'), ('2', '其他')], max_length=1, verbose_name='房屋状态'),
        ),
    ]