from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cabinet, name="cabinet"),
    path('info/', views.cabinet_info, name="cabinet_info"),
    path('orders/', views.cabinet_orders, name="cabinet_orders"),
    path('admin/', views.cabinet_admin, name="cabinet_admin"),
    path('admin/info/', views.cabinet_admin_info, name="cabinet_admin_info"),
    path('admin/orders/', views.cabinet_admin_orders, name="cabinet_admin_orders"),
    path('admin/management/', views.cabinet_admin_management, name="cabinet_admin_management")
]
