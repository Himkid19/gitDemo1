# Generated by Django 2.2.4 on 2019-09-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0006_auto_20190929_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_info',
            name='house_image',
            field=models.ImageField(upload_to='', verbose_name='房屋图片'),
        ),
        migrations.AlterField(
            model_name='house_info',
            name='status',
            field=models.CharField(choices=[('0', '闲置'), ('1', '已售'), ('2', '其他')], max_length=1, verbose_name='房屋状态'),
        ),
    ]