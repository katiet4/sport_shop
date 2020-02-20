from django.shortcuts import render
from Goods.models import About_goods, Goods_of_user
from django.http import HttpResponseRedirect
# Create your views here.
def basket(request):
	if request.user.is_authenticated:
		aunt = True
	else:
		aunt = False
	count = 0
	goodsFullInfo = []
	idForDelete = []
	try:
		goods = Goods_of_user.objects.filter(userName = request.session["user"])
		count = len(goods)
		for i in goods:
			good = About_goods.objects.get(id = i.goodId)
			goodsFullInfo.append({"name" : good.name,
								  "price" : good.price,
								  "image" : good.image,
								  "id" : i.id})
		return render(request, "BasketTemp/basket.html", {"count":count,
														  "goods": goodsFullInfo,
														  "aunt" : aunt,
														  "idForDelete" : idForDelete})
	except Exception as e:
		return render(request, "BasketTemp/basket.html", {"count":count,
														  "goods": goodsFullInfo,
														  "aunt" : aunt,
														  "idForDelete" : idForDelete})

def delete(request, ID):
	try:
		Goods_of_user.objects.get(id = ID).delete()
	except Exception as e:
		pass
	return HttpResponseRedirect("/basket/")

	