
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cabinet, name="cabinet"),
    path('settings/', views.cabinet_settings, name="cabinet_settings"),
    path('settings/upload_file', views.cabinet_settings_upload_file, name="cabinet_settings_upload_file"),
    path('settings/reset_password', views.cabinet_settings_reset_password, name="cabinet_settings_reset_password"),
    path('settings/reset_username', views.cabinet_settings_reset_username, name="cabinet_settings_reset_username"),
    path('info/', views.cabinet_info, name="cabinet_info"),
    path('orders/', views.cabinet_orders, name="cabinet_orders"),
    path('admin/', views.cabinet_admin, name="cabinet_admin"),
    path('admin/info/', views.cabinet_admin_info, name="cabinet_admin_info"),
    path('admin/orders/', views.cabinet_admin_orders, name="cabinet_admin_orders"),
    path('admin/management/', views.cabinet_admin_management, name="cabinet_admin_management")
]
