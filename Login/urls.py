from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('recover_password/', views.recover_password, name="recover_password"),
    re_path("recover_password/(?P<recoverID>[0-9a-zA-Z]{33})/", views.recover_set_new_password, name="recover_set_new_password")
]
