from django.shortcuts import render
from django.contrib.auth.models import User
def cabinet(request):
    if request.user.is_authenticated:
        ID = request.session['id']
        usr = User.objects.get(id = ID)
        return render(request, "CabinetTemp/cabinet.html", {"aunt":True,
        													"admin" : usr.is_staff,
                                                            "name"  : usr.username,
                                                            "id"    : usr.id,
                                                            "last_join"    : usr.date_joined,
        													"email" : usr.email})
    else:
        return HttpResponseRedirect("/main")
