from django.shortcuts import render
from django.contrib.auth.models import User


def rendering(request, what):
    if request.user.is_authenticated:
        ID = request.session['id']
        usr = User.objects.get(id = ID)
        return render(request, "CabinetTemp/"+what+".html", {"aunt":True,
                                                                "admin" : usr.is_staff})
    else:
        return HttpResponseRedirect("/main")



def cabinet(request):
    return rendering(request, "cabinet")



def cabinet_info(request):
    if request.user.is_authenticated:
        ID = request.session['id']
        usr = User.objects.get(id = ID)
        return render(request, "CabinetTemp/infoblock.html", {"aunt":True,
                                                                "admin" : usr.is_staff,
                                                                "name"  : usr.username,
                                                                "id"    : usr.id,
                                                                "last_join"    : usr.date_joined,
                                                                "email" : usr.email})
    else:
        return HttpResponseRedirect("/main")

def cabinet_orders(request):
    return rendering(request, "ordblock")

def cabinet_admin(request):
    return rendering(request, "adminblock")

def cabinet_admin_info(request):
    return rendering(request, "adminblock_info")

def cabinet_admin_orders(request):
    return rendering(request, "adminblock_orders")

def cabinet_admin_management(request):
    return rendering(request, "adminblock_management")