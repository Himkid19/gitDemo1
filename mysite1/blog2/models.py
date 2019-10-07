from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    org = models.CharField("organization",max_length=60,blank=True)
    telephone = models.CharField("Telephone",max_length=50,blank=True)

    class Meta:
        verbose_name ="UserProfile"

    def __str__(self):
        return self.user.__str__()

    def __unicode__(self):
        return self.username

class HouseInfo(models.Model):
    house_no = models.CharField(verbose_name="房号",max_length=5,default=None,unique=True)
    house_image = models.ImageField(verbose_name="房屋图片")
    width = models.CharField(verbose_name="大小",max_length=10)
    height = models.CharField(verbose_name="高",max_length=10)
    direction = models.CharField(verbose_name="描述",max_length=256)
    user = models.ForeignKey("UserProfile",verbose_name="所属用户",on_delete=models.CASCADE,null=True,blank=True,)
    house_status = (
        ('0',"闲置"),('1',"已售"),('2',"其他")
    )
    status = models.CharField(max_length=1,verbose_name="房屋状态",choices=house_status)
    def __str__(self):
        return self.house_no.__str__()
    def __unicode__(self):
        return self.house_no


class monthly_pay(models.Model):
    user = models.ForeignKey("UserProfile",verbose_name="用户",on_delete=models.CASCADE,)
    water_rate = models.CharField(verbose_name="水费",max_length=30)
    power_rate = models.CharField(verbose_name="电费",max_length=30)
    house_rent = models.CharField(verbose_name="房费",max_length=30)
    else_rate = models.CharField(verbose_name="其他费用",max_length=30,null=True,blank=True)
    remark = models.CharField(verbose_name="备注",max_length=30,null=True,blank=True)
    create_date = models.DateField
    house_no = models.ForeignKey(HouseInfo,to_field="house_no",on_delete=models.CASCADE,default=None)
    payment_choice =(('0','未支付/欠费'),('1','已支付'),('2','异常'))
    payment_status = models.CharField(verbose_name='支付状态',choices=payment_choice,max_length=3,default='0')

