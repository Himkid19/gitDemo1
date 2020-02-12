from blog2.models import UserProfile


def group_name(request):
    global group_name
    user = request.user
    Groups = user.groups.all()
    try:
        org = UserProfile.objects.get(user=user).org
    except:
        org = ''
    for i in Groups:
        group_name = str(i)
    return {'group_name':group_name,'org':org}



