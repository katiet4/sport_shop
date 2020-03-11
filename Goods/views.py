from django.shortcuts import render
from Goods.models import About_goods, Goods_of_user
from django.http import HttpResponseRedirect

class views:

    def __init__(self):
        self.aunt = False

    def rendering(self, category, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        goods = About_goods.objects.filter(category=category).order_by("-id")


        return render(request, 'MainTemp/main.html', {"aunt":self.aunt,
                        "goods":goods})

    def goods(self, request):
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        goods = About_goods.objects.all().order_by("-id")
        return render(request, 'MainTemp/main.html', {"aunt":self.aunt,
                        "goods":goods})

    def games_with_balls(self, request):

        return self.rendering("games_with_balls", request)

    def bikes(self, request):
        return self.rendering("bikes", request)

    def dumbbells_and_rods(self, request):
        return self.rendering("dumbbells_and_rods", request)

    def fighting_art(self, request):
        return self.rendering("fighting_art", request)

    def premium_attributes(self, request):
        return self.rendering("premium_attributes", request)

    def billiards(self, request):
        return self.rendering("billiards", request)

    def jumpers(self, request):
        return self.rendering("jumpers", request)

    def desktop_games(self, request):
        return self.rendering("desktop_games", request)

    def baseball(self, request):
        return self.rendering("baseball", request)

    def espandery(self, request):
        return self.rendering("espandery", request)

    def swimming(self, request):
        return self.rendering("swimming", request)

    def darts(self, request):
        return self.rendering("darts", request)

    def buy(self, request, ID):
        try:
            if(Goods_of_user.objects.filter(userName = request.session["user"], goodId = ID)):
                return HttpResponseRedirect("/store")

            goodOfUser = Goods_of_user(userName = request.session["user"],
                                        goodId = ID)
            goodOfUser.save()
        except Exception as e:
            return HttpResponseRedirect("/store/"+ID)
        return HttpResponseRedirect("/store")
    def goods_by_id(self, request, ID):
        good = About_goods.objects.get(id = ID)
        if request.user.is_authenticated:
            self.aunt = True
        else:
            self.aunt = False
        return render(request, "BuyTemp/buy.html", {"price"      :good.price,
                                                    "name"       :good.name,
                                                    "description":good.description,
                                                    "image"      :good.image,
                                                    "count"      :good.count,
                                                    "id"         :ID,
                                                    "aunt"       :self.aunt})
