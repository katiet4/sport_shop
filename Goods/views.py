from django.shortcuts import render
from Goods.models import About_goods, Goods_of_user
from Cabinet.models import Comments
from Login.models import Profile_of_user
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from Main.basket_new_goods import calculate_new
from math import ceil
import json
class views:

    def __init__(self):
        self.aunt = False
        self.countOfPages = 0

    def rendering(self, category, request):
        
        newGoods = ""
        if request.user.is_authenticated:
            count = calculate_new(request.session["user"])
            newGoods = "" if count == 0 else count
            self.aunt = True
        else:
            self.aunt = False
        goods = ""
        if category == "All":
            goods = About_goods.objects.all().order_by("-id")
        else:
            goods = About_goods.objects.filter(category=category).order_by("-id")

        #Перелистование страниц   
        count_pages = ceil(len(goods)/8)
        num_page = 1
        
        if request.GET:
            num_page = int(request.GET["page"])
            goods = goods[(num_page-1) * 8 : num_page * 8]
        else:
            goods = goods[:8]
        show_pages_result = [i for i in range(num_page - 2, num_page + 3) if (i > 0 and i <= count_pages)]
        if (show_pages_result == []):
            show_pages_result = [1]
        return render(request, 'MainTemp/main.html', {"aunt":self.aunt,
                        "goods":goods,
                        "goodsInBasket" : newGoods,
                        "pages" : show_pages_result,
                        "middleNumber" : num_page})

    def goods(self, request):
        return self.rendering("All", request)

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
                                        goodId = ID,
                                        checked = 0)
            goodOfUser.save()
        except Exception as e:
            return HttpResponseRedirect("/store/"+ID)
        return HttpResponseRedirect("/store")
        
    def goods_by_id(self, request, ID):
        newGoods = ""
        if request.user.is_authenticated:
            count = calculate_new(request.session["user"])
            newGoods = "" if count == 0 else count
            self.aunt = True
        else:
            self.aunt = False
        try:
            comments = Comments.objects.filter(goodId = ID).order_by("-id")
            good = About_goods.objects.get(id = ID)
        except Exception as e:
            pass

        ratingMiddle = 0
        allInfoAboutComments = []
        for i in comments:
            infoAboutComments = {}
            ratingMiddle+= float(i.rating)
            try:
                profile = Profile_of_user.objects.get(userId = i.userId)
                username = User.objects.get(id = i.userId).username
                infoAboutComments['ava'] = profile.userImg
                infoAboutComments['status'] = profile.userStatus
                infoAboutComments['name'] = username
                infoAboutComments['rating'] = i.rating
                infoAboutComments['comment'] = i.comment
                allInfoAboutComments.append(infoAboutComments)
            except Exception as e:
                pass

        if request.POST:
            ratings = request.POST["send_rating"]
            commentSended = request.POST["comment"]
            ratingMiddle += float(ratings)
            good.rating = str(round(ratingMiddle/(len(comments)+1), 2))
            good.save()
            comm = Comments(goodId = ID, userId=request.session["id"], comment = commentSended, rating = ratings)
            comm.save()
            return HttpResponseRedirect("/store/goods/"+str(ID))
        return render(request, "BuyTemp/buy.html", {"price"      :good.price,
                                                    "name"       :good.name,
                                                    "description":good.description.split("\n"),
                                                    "image"      :good.image,
                                                    "count"      :good.count,
                                                    "id"         :ID,
                                                    "comment"    :allInfoAboutComments,
                                                    "rating"     :good.rating,
                                                    "aunt"       :self.aunt,
                                                     "goodsInBasket" : newGoods})
