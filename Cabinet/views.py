<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.models import User
from Goods.models import About_goods
from Cabinet.models import Orders
from django.http import HttpResponseRedirect

def checkAunt(request, what, dict, admin = 0):
    if request.user.is_authenticated:
        ID = request.session['id']
        usr = User.objects.get(id = ID)
        dict['admin'] = usr.is_staff
        if(admin):
            if(dict['admin']):
                return render(request, "CabinetTemp/"+ what +".html", dict)
            else:
                return HttpResponseRedirect("/cabinet")
        return render(request, "CabinetTemp/"+ what +".html", dict)
    return HttpResponseRedirect("/main")

def cabinet(request):
        dict = {"aunt":True}
        return checkAunt(request, "cabinet", dict)

def cabinet_info(request):
    ID = request.session['id']
    usr = User.objects.get(id = ID)
    dict = {"aunt":True,
            "name"  : usr.username,
            "id"    : usr.id,
            "last_join"    : usr.date_joined,
            "email" : usr.email}
    return checkAunt(request, "infoblock", dict)


def cabinet_orders(request):
    orders = Orders.objects.filter(userName = request.session["user"]).order_by('-id')
    alreadyOrders = []
    allNumOfOrders = set()
    for i in orders:
        allNumOfOrders.add(i.numberOfOrder)
    for i in allNumOfOrders:
        order = {}
        goods = []
        orders = Orders.objects.filter(numberOfOrder = i).order_by('-id')
        for j in orders:
            order['result'] = j.result
            order['userName'] = j.userName
            AboutGood = About_goods.objects.get(id = j.goodId)
            goods.append({"good" : AboutGood,
                          'count' : j.count,
                          "price": j.count*AboutGood.price})
        order['status'] = j.status
        order['numberOfOrder'] = i
        order['goods'] = goods
        alreadyOrders.append(order)

    dict = {"aunt":True, "orders" : alreadyOrders}
    return checkAunt(request, "ordblock", dict)

def cabinet_admin(request):
    dict = {"aunt":True}
    return checkAunt(request, "adminblock", dict, 1)

def cabinet_admin_info(request):
    orders = Orders.objects.all().order_by('-id')
    statusOfOrders = {"Отменено" : 0, "Подтверждение оплаты" : 0,
                    "Оплачено" : 0, "Отправлено" : 0, "Завершено" : 0}
    allNumOfOrders = set()
    for i in orders:
        allNumOfOrders.add(i.numberOfOrder)
    for i in allNumOfOrders:
        orders = Orders.objects.filter(numberOfOrder = i).order_by('-id')
        for j in orders:
            statusOfOrders[j.status] += 1
            break
    dict = {"aunt":True, "canceled" : statusOfOrders["Отменено"],
            "paymentConfirmation" : statusOfOrders["Подтверждение оплаты"],
            "paid" : statusOfOrders["Оплачено"],
            "sent" : statusOfOrders["Отправлено"],
            "completed" : statusOfOrders["Завершено"]}
    return checkAunt(request, "adminblock_info", dict, 1)

def cabinet_admin_orders(request):
    if request.POST:
        try:
            id = request.POST["hiddenId"]
            stat = request.POST["stat"]
            orders = Orders.objects.filter(numberOfOrder = id)
            for i in orders:
                i.status = stat
                i.save()

        except Exception as e:
            print(e)
            search = request.POST["search"]
            orders = Orders.objects.filter(numberOfOrder = search).order_by('-id')
            if search == "":
                orders = Orders.objects.all().order_by('-id')
    orders = Orders.objects.all().order_by('-id')
    alreadyOrders = []
    allNumOfOrders = set()



    for i in orders:
        allNumOfOrders.add(i.numberOfOrder)
    for i in allNumOfOrders:
        order = {}
        goods = []

        orders = Orders.objects.filter(numberOfOrder = i).order_by('-id')
        for j in orders:
            order['result'] = j.result
            order['userName'] = j.userName
            AboutGood = About_goods.objects.get(id = j.goodId)
            goods.append({"good" : AboutGood,
                          'count' : j.count,
                          "price": j.count*AboutGood.price})
        order['status'] = j.status
        order['numberOfOrder'] = i
        order['goods'] = goods
        alreadyOrders.append(order)

    dict = {"aunt":True, "orders" : alreadyOrders}
    return checkAunt(request, "adminblock_orders", dict, 1)

def cabinet_admin_management(request):
    dict = {"aunt":True}
    return checkAunt(request, "adminblock_management", dict, 1)
=======
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
>>>>>>> 262c75b71940de3e2525e01687e27ef3e4ee3244
