# Generated by Django 2.1.4 on 2019-11-28 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0022_auto_20191128_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='hydropower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(blank=True, max_length=10, null=True, verbose_name='电量')),
                ('water', models.CharField(blank=True, max_length=10, null=True, verbose_name='水量')),
            ],
        ),
        migrations.RemoveField(
            model_name='houseinfo',
            name='power',
        ),
        migrations.RemoveField(
            model_name='houseinfo',
            name='water',
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='last_time',
            field=models.DateField(auto_now=True, verbose_name='最近更新时间'),
        ),
        migrations.AddField(
            model_name='hydropower',
            name='house_no',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog2.HouseInfo', to_field='house_no'),
        ),
    ]
