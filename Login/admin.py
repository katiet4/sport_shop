from django.contrib import admin
from Login.models import Profile_of_user, URL_for_reset
# Register your models here.
admin.site.register(Profile_of_user)
admin.site.register(URL_for_reset)
