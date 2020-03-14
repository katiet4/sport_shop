from django.contrib import admin
from Goods.models import About_goods, Goods_of_user, Comments
# Register your models here.
admin.site.register(About_goods)
admin.site.register(Goods_of_user)
admin.site.register(Comments)
