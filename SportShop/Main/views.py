from django.shortcuts import render
from Goods.models import About_goods
# Create your views here.
class views:
    def __init__(self):
        self.aunt = False

    def rendering(self, request):

        goods = About_goods.objects.all().order_by("-id")[:12]
        goods_for_site = [[]]
        num = 0
        for i in goods:
            goods_for_site[num].append(i)
            if (len(goods_for_site[num]) == 4):
                goods_for_site.append([])
                num+=1


        return render(request, 'MainTemp/main.html', {"aunt":self.aunt,
                        "goods":goods_for_site})
    def main(self, request):
        
        if request.user.is_authenticated:
            self.aunt = True
        else:
        	self.aunt = False
        return self.rendering(request)
