from django.shortcuts import render
from Main.basket_new_goods import calculate_new
import json
import requests
# Create your views here.
class views:
    def __init__(self):
        self.aunt = False

    def rendering(self, request, newGoods):
        sportNews = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=sports&apiKey=4df71164a27d4abb98b0d0c9b3743e23")
        return render(request, 'NewsTemp/news.html', {"aunt":self.aunt, "news":sportNews.json()["articles"], "goodsInBasket" : newGoods, })
    def main(self, request):
        newGoods = ""
        if request.user.is_authenticated:
            self.aunt = True
            count = calculate_new(request.session["user"])
            newGoods = "" if count == 0 else count
        else:
        	self.aunt = False
        return self.rendering(request, newGoods)
