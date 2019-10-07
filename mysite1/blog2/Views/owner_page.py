from django.shortcuts import render,redirect
from blog2.models import UserProfile,User,Group

# 待审核列表
def Waiting_Audit_Info(request):
    v_Groups = Group.objects.get(name='游客')
    users = v_Groups.user_set.all()
    Groups_display = str(v_Groups)

    r_Groups = Group.objects.get(name='租客')
    r_users = r_Groups.user_set.all()
    r_display = str(r_Groups)
    return render(request,'waiting_audit_info.html',locals())
# 审核租客信息
def Audit_tenant_Info(request):
    username = request.POST.get('username')

    Group.objects.filter(user=username).update(name='租客')
    return redirect('/index/waiting_list')
def set_count(request):
    pass