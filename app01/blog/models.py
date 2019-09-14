from django.db import models

# Create your models here.

# 出租屋屋号集合
class Rental_No_set(models.Model):
    Rental_No = models.IntegerField(max_length=5)
    Localtion = models.CharField(max_length=60)

# 房费
class Cost(models.Model):
    Water_Rate = models.IntegerField(max_length=256)
    Electric_Rate = models.IntegerField(max_length=256)
    Room_Rate = models.IntegerField(max_length=256)
    Rental_No = models.ForeignKey("Rental_No_set",on_delete=models.CASCADE)

class User_Info(models.Model):

    login_user_name = models.CharField(max_length=256)
    login_Pw = models.CharField(max_length=256)
    phone_No = models.IntegerField(max_length=60)

# 租赁人员信息
class leasee_info(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    ID_card_No = models.IntegerField(max_length=128)
    sex = models.BooleanField(default=True)
    Rental_No = models.ForeignKey("Rental_No_set",on_delete=models.CASCADE)
    cost = models.IntegerField(max_length=32)
    user_name = models.CharField(max_length=32)
    phone_No = models.ForeignKey('User_Info',on_delete=models.CASCADE)





