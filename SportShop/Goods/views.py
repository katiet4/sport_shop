from django.shortcuts import render
from Goods.models import About_goods
# Create your views here.
class views:

    def __init__(self):
        self.aunt = False

    def rendering(self, category, request):

        goods = About_goods.objects.filter(category=category).order_by("-id")
        goods_for_site = [[]]
        num = 0
        for i in goods:
            goods_for_site[num].append(i)
            if (len(goods_for_site[num]) == 4):
                goods_for_site.append([])
                num+=1


        return render(request, 'MainTemp/main.html', {"aunt":self.aunt,
                        "goods":goods_for_site})

    def goods(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return render(request, 'MainTemp/main.html', {"aunt":aunt})

    def games_with_balls(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("games_with_balls", request)

    def bikes(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("bikes", request)

    def dumbbells_and_rods(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("dumbbells_and_rods", request)

    def fighting_art(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("fighting_art", request)

    def premium_attributes(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("premium_attributes", request)

    def billiards(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("billiards", request)

    def jumpers(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("jumpers", request)

    def desktop_games(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("desktop_games", request)

    def baseball(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("baseball", request)

    def espandery(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("espandery", request)

    def swimming(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("swimming", request)

    def darts(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return self.rendering("darts", request)
