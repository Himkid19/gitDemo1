


def group_name(request):
    global group_name
    user = request.user
    Groups = user.groups.all()
    for i in Groups:
        group_name = str(i)
    return {'group_name':group_name}