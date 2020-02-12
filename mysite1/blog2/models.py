from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
from django.utils import timezone


class organization(models.Model):
    loaction = models.CharField('Loaction',max_length=60,blank=True)
    class Meta:
        verbose_name ="organization"

    def __str__(self):
        return self.loaction.__str__()

    def __unicode__(self):
        return self.loaction

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    org = models.ForeignKey(organization,verbose_name='org',on_delete=models.CASCADE)
    telephone = models.CharField("Telephone",max_length=50,blank=True)
    openid = models.CharField('openid',max_length=64,blank=True)
    session_key = models.CharField('session_key',max_length=64,blank=True)
    uuid = models.CharField('uuid',max_length=64,blank=True)
    class Meta:
        verbose_name ="UserProfile"

    def __str__(self):
        return self.user.__str__()

    def __unicode__(self):
        return self.username

class HouseInfo(models.Model):
    house_no = models.CharField(verbose_name="房号",max_length=5,default=None,unique=True)
    house_image = models.ImageField(verbose_name="房屋图片",upload_to="img/")
    width = models.CharField(verbose_name="大小",max_length=10)
    height = models.CharField(verbose_name="高",max_length=10)
    direction = models.CharField(verbose_name="描述",max_length=256)

    user = models.ForeignKey(User,verbose_name="所属用户",on_delete=models.CASCADE,null=True,blank=True)
    house_status = (
        ('0',"闲置"),('1',"已售"),('2',"其他")
    )
    status = models.CharField(max_length=1,verbose_name="房屋状态",choices=house_status)

    chair = models.CharField(max_length=4,verbose_name='椅子数目',null=True,blank=True)
    table = models.CharField(max_length=4,verbose_name='桌子数目',null=True,blank=True)
    bed = models.CharField(max_length=4,verbose_name='床数目',null=True,blank=True)
    blower = models.CharField(max_length=4,verbose_name='风扇数量',null=True,blank=True)
    aircon = models.CharField(max_length=4,verbose_name='空调数量',null=True,blank=True)
    else_support = models.CharField(max_length=256,verbose_name='其他配套设施补充',null=True,blank=True)
    last_time = models.DateField('最近更新时间',auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.house_no.__str__()
    def __unicode__(self):
        return self.house_no

class hydropower(models.Model):
    house_no = models.ForeignKey(HouseInfo,to_field="house_no",on_delete=models.CASCADE,default=None)
    power = models.CharField(max_length=10, verbose_name='电量', null=True, blank=True)
    water = models.CharField(max_length=10, verbose_name='水量', null=True, blank=True)
    last_time = models.DateField('最近更新时间', auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.house_no.__str__()
    def __unicode__(self):
        return self.house_no

class monthly_pay(models.Model):

    water_rate = models.CharField(verbose_name="水费",max_length=30)
    power_rate = models.CharField(verbose_name="电费",max_length=30)
    house_rent = models.CharField(verbose_name="房费",max_length=30)
    else_rate = models.CharField(verbose_name="其他费用",max_length=30,null=True,blank=True)
    remark = models.CharField(verbose_name="备注",max_length=30,null=True,blank=True)
    create_time = models.DateField('创建时间', auto_now_add=True)
    last_time = models.DateField('最后修改时间',auto_now=True)
    house_no = models.ForeignKey(HouseInfo,to_field="house_no",on_delete=models.CASCADE,default=None)
    payment_choice =(('0','未支付/欠费'),('1','已支付'),('2','异常'))
    payment_status = models.CharField(verbose_name='支付状态',choices=payment_choice,max_length=3,default='0')
    total = models.CharField(verbose_name='总金额',max_length=30,default='0')

    def __str__(self):
        return self.house_no.__str__()
    def __unicode__(self):
        return self.house_no.__str__()

class Application_list(models.Model):
    status_type = (('0','待审核'),('1','审核通过'),('2','审核不通过'))
    status = models.CharField(verbose_name='申请状态',max_length=5,choices=status_type,default='0')

    type_choice = (('0','退房申请'),('1','房屋配套申请'),('2','其他申请'))
    type = models.CharField(verbose_name='申请类型',max_length=50,choices=type_choice,default='0')
    username = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE,default=None)
    content = models.CharField(verbose_name='申请内容',max_length=300,default='')
    remark = models.CharField(verbose_name='备注',max_length=300,null=True,blank=True)
    create_time = models.DateField('创建时间',auto_now_add=True)
    last_time = models.DateField('最新编辑时间',auto_now=True)