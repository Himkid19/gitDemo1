from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    org = models.CharField("organization",max_length=60,blank=True)
    telephone = models.CharField("Telephone",max_length=50,blank=True)

    class Meta:
        verbose_name ="UserProfile"

        def __str__(self):
            return self.user.__str__()