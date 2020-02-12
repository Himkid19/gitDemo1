from django.contrib import admin
from .models import UserProfile,HouseInfo,monthly_pay,hydropower,Application_list,organization
# Register your models here.
class House_display(admin.ModelAdmin):
    list_display = ['house_no','user','status']


class rate_display(admin.ModelAdmin):
    list_display = ['house_no','payment_status','create_time','last_time']

class hydropower_display(admin.ModelAdmin):
    list_display = ['house_no','water','power','last_time']


admin.site.register(hydropower,hydropower_display)
admin.site.register(UserProfile)
admin.site.register(organization)
admin.site.register(monthly_pay,rate_display)
admin.site.register(HouseInfo,House_display)
admin.site.register(Application_list)