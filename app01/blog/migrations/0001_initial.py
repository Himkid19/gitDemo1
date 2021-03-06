# Generated by Django 2.2.4 on 2019-08-30 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental_No_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rental_No', models.IntegerField(max_length=5)),
                ('Localtion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_user_name', models.CharField(max_length=256)),
                ('login_Pw', models.CharField(max_length=256)),
                ('phone_No', models.IntegerField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='leasee_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(max_length=32)),
                ('ID_card_No', models.IntegerField(max_length=128)),
                ('sex', models.BooleanField(default=True)),
                ('cost', models.IntegerField(max_length=32)),
                ('user_name', models.CharField(max_length=32)),
                ('phone_No', models.IntegerField(max_length=32)),
                ('Rental_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Rental_No_set')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Water_Rate', models.IntegerField(max_length=256)),
                ('Electric_Rate', models.IntegerField(max_length=256)),
                ('Room_Rate', models.IntegerField(max_length=256)),
                ('Rental_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Rental_No_set')),
            ],
        ),
    ]
