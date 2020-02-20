from django.shortcuts import render
from Main.models import News
# Create your views here.
class views:
    def __init__(self):
        self.aunt = False

    def rendering(self, request):
        news = News.objects.all().order_by("-id")[:5]
        for i in range(0,len(news)):
            news[i].text = news[i].text[0:300] + "..."
        return render(request, 'NewsTemp/news.html', {"aunt":self.aunt, "news":news})
    def main(self, request):

        if request.user.is_authenticated:
            self.aunt = True
        else:
        	self.aunt = False
        return self.rendering(request)
