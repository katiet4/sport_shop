from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from .GetShortURL import generateSURL
from .models import URL_for_reset
import smtplib
import socket

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/main")
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                request.session["id"] = user.id
                request.session["user"] = user.username
                return HttpResponseRedirect("/main")

            else:
                return render(request, "LoginTemp/login.html", {"retry":"Неверный логин/пароль"}) #Возвращает, если такого пользователя не существует
        else:
            return render(request, "LoginTemp/login.html")
def logout(request):
    auth.logout(request)
    request.session["user"] = None
    request.session["id"] = 0
    return HttpResponseRedirect("/login")

def recover_password(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/main")
    else:
        if request.POST:
            email = request.POST["email"]
            if  (User.objects.filter(email = email).exists()):
                user = User.objects.get(email = email)
                print()
                if(URL_for_reset.objects.filter(userId = user.id).exists()):
                    return HttpResponseRedirect("/login")
                url = generateSURL(URL_for_reset)
                addUrlToBD = URL_for_reset(codeURL = url, userId = user.id)
                addUrlToBD.save()

                HOSTNAME = '127.0.0.1:8000' # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOUR HOSTNAME

                m = ("To restore your password, follow this link: http://" +
                        HOSTNAME + "/login/recover_password/" + url)
                try:
                    smtpObj = smtplib.SMTP('smtp.mail.ru', 587) # connect tot server
                    smtpObj.starttls() # encrypt message
                    smtpObj.login('sportshop174@inbox.ru','KSJdjak3j;kAJWfje') # connect to account
                    smtpObj.sendmail('sportshop174@inbox.ru',
                                    email,
                                    m) # sending message
                    smtpObj.quit()
                except Exception as e:
                    pass


    return HttpResponseRedirect("/login")

def recover_set_new_password(request, recoverID):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/main")
    else:
        if(URL_for_reset.objects.filter(codeURL = recoverID).exists()):
            if request.POST:
                newPass = request.POST['new']
                url = URL_for_reset.objects.get(codeURL = recoverID)
                user = User.objects.get(id = url.userId)
                user.set_password(newPass)
                user.save()
                url.delete()
            else:
                return render(request, "LoginTemp/recover.html")
        return HttpResponseRedirect("/login")
