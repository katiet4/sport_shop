
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.basket, name="basket"),
    path('buy_all', views.buy_all, name="buy_all"),
    re_path('delete/(?P<ID>[0-9]{1,10})/', views.delete, name="delete")
]
