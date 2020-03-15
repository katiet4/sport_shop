from django.shortcuts import render
from django.contrib.auth.models import User
from Goods.models import About_goods
from Login.models import Profile_of_user
from Cabinet.models import Orders
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage
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
    return HttpResponseRedirect("/cabinet/info")
def cabinet_info(request):
    try:
        ID = request.session['id']
        usr = User.objects.get(id = ID)
    except Exception as e:
        return HttpResponseRedirect("/main")
    image = Profile_of_user.objects.get(userId = request.session['id']).userImg
    dict = {"aunt":True,
            "name"  : usr.username,
            "id"    : usr.id,
            "last_join"    : usr.date_joined,
            "image" : image,
            "email" : usr.email}
    return checkAunt(request, "infoblock", dict)


def cabinet_orders(request):
    try:
        orders = Orders.objects.filter(userName = request.session["user"]).order_by('-id')
    except Exception as e:
        return HttpResponseRedirect("/main")
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
    return HttpResponseRedirect("/cabinet/admin/info")

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
            print(2)
            for i in orders:
                i.status = stat
                i.save()
            orders = Orders.objects.all().order_by('-id')
        except Exception as e:
            print(1)
            search = request.POST["search"]
            print(search)
            orders = Orders.objects.filter(numberOfOrder = search).order_by('-id')
            if search == "":
                orders = Orders.objects.all().order_by('-id')
    else:
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



def cabinet_settings(request):
    profile = Profile_of_user.objects.get(userId = request.session['id'])
    dict = {"aunt":True, "ava" : profile.userImg}
    return checkAunt(request, "settings", dict)



def cabinet_settings_upload_file(request):
    if request.user.is_authenticated:
        try:
            if request.method == 'POST' and request.FILES['file']:
                file = request.FILES['file']
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                uploaded_file_url = fs.url(filename)
                profile = Profile_of_user.objects.get(userId = request.session['id'])
                profile.userImg = "/static" + uploaded_file_url
                profile.save()
        except Exception as e:
            pass
        return HttpResponseRedirect("/cabinet/settings")
    else:
        return HttpResponseRedirect("/main")
def cabinet_settings_reset_password(request):
    if request.user.is_authenticated:
        try:
            if request.POST:
                oldPass = request.POST['old']
                newPass = request.POST['new']
                user = User.objects.get(id = request.session['id'])
                if(check_password(oldPass,user.password)):
                    user.set_password(newPass)
                    user.save()
                userLogin = auth.authenticate(username=user.username, password=newPass)
                if userLogin is not None and userLogin.is_active:
                    auth.login(request, userLogin)
                    request.session["id"] = userLogin.id
                    request.session["user"] = userLogin.username

        except Exception as e:
            pass
        return HttpResponseRedirect("/cabinet/settings")
    else:
        return HttpResponseRedirect("/main")

def cabinet_settings_reset_username(request):
    if request.user.is_authenticated:
        try:
            if request.POST:
                newLogin = request.POST['newusername']
                newEmail = request.POST['newemail']
                password = request.POST['password']
                user = User.objects.get(id = request.session['id'])
                if(check_password(password,user.password)):
                    if(newLogin != ""):
                        user.username = newLogin
                    if(newEmail != "" and User.objects.filter(email = newEmail).exists() == False):
                        user.email = newEmail
                    user.save()
                    userLogin = auth.authenticate(username=user.username, password=password)
                    if userLogin is not None and userLogin.is_active:
                        auth.login(request, userLogin)
                        request.session["id"] = userLogin.id
                        request.session["user"] = userLogin.username

        except Exception as e:
            pass
        return HttpResponseRedirect("/cabinet/settings")
    else:
        return HttpResponseRedirect("/main")
