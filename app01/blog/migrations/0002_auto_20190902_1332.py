# Generated by Django 2.2.4 on 2019-09-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leasee_info',
            name='phone_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User_Info'),
        ),
    ]
