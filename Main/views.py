from django.shortcuts import render
from Main.basket_new_goods import calculate_new
import json
import requests
# Create your views here.
class views:
    def __init__(self):
        self.aunt = False
        self.sportNews = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=sports&apiKey=4df71164a27d4abb98b0d0c9b3743e23")
        try:
            self.sportNews = self.sportNews.json()
        except Exception as e:
            self.sportNews = {"articles":[
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"},
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"},
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"},
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"},
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"},
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"},
            {"source": {"name": "Business-gazeta.ru"},"author": "БИЗНЕС Online", "title": "В Беларуси 23 игрока хоккейной команды заразились COVID-19 - БИЗНЕС Online","description": "23 игрока белорусского хоккейного клуба &laquo;Неман&raquo; заразились COVID-19, сообщает Tribuna.com со&nbsp;ссылкой на&nbsp;телеграм-канал NEXTA Live.","url": "https://www.business-gazeta.ru/news/465888","urlToImage": "https://cdn2.business-gazeta.ru/files/news/cf/465888.jpg"}]}
    
    def rendering(self, request, newGoods):
        return render(request, 'NewsTemp/news.html', {"aunt":self.aunt, "news":self.sportNews["articles"], "goodsInBasket" : newGoods })
    
    def main(self, request):
        newGoods = ""
        if request.user.is_authenticated:
            self.aunt = True
            count = calculate_new(request.session["user"])
            newGoods = "" if count == 0 else count
        else:
        	self.aunt = False
        return self.rendering(request, newGoods)
