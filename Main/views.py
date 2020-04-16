from django.shortcuts import render
from Main.models import News
from Main.basket_new_goods import calculate_new
# Create your views here.
class views:
    def __init__(self):
        self.aunt = False

    def rendering(self, request, newGoods):
        news = News.objects.all().order_by("-id")[:5]
        for i in range(0,len(news)):
            news[i].text = news[i].text[0:300] + "..."
        return render(request, 'NewsTemp/news.html', {"aunt":self.aunt, "news":news, "goodsInBasket" : newGoods })
    def main(self, request):
        newGoods = ""
        if request.user.is_authenticated:
            self.aunt = True
            count = calculate_new(request.session["user"])
            newGoods = "" if count == 0 else count
        else:
        	self.aunt = False
        return self.rendering(request, newGoods)
