from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

def registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/main")
    else:
        if request.POST:
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            if  (User.objects.filter(username = username).exists() or
                User.objects.filter(email = email).exists()):
                return render(request, "RegTemp/registration.html") # Возвращать, если такой пользователь уже существует

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            # Вход в систему
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                request.session["id"] = user.id
                request.session["user"] = user.username
                return HttpResponseRedirect("/main")
                
        return render(request, "RegTemp/registration.html")

# Create your views here.s
# from django.contrib.auth.models import User
# >>> user = User.objects.create_user(username='john',
# ...                                 email='jlennon@beatles.com',
# ...                                 password='glass onion')
