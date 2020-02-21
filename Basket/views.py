from django.shortcuts import render
from Goods.models import About_goods, Goods_of_user
from Cabinet.models import Orders
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
		for i in goods:

			good = About_goods.objects.get(id = i.goodId)
			goodsFullInfo.append({"name" : good.name,
								  "price" : good.price,
								  "image" : good.image,
								  "idForPlusAndMinus" : count,
								  "id" : i.id})
			count+=1
		return render(request, "BasketTemp/basket.html", {"count":count,
														  "goods": goodsFullInfo,
														  "aunt" : aunt,
														  "idForDelete" : idForDelete})
	except Exception as e:
		return render(request, "BasketTemp/basket.html", {"count":count,
														  "goods": goodsFullInfo,
														  "aunt" : aunt,
														  "idForPlusAndMinus" : count,
														  "idForDelete" : idForDelete})

def delete(request, ID):
	try:
		Goods_of_user.objects.get(id = ID).delete()
	except Exception as e:
		pass
	return HttpResponseRedirect("/basket/")

def buy_all(request):
	if request.POST:
		num = int(request.POST['b'])
		orders = Orders.objects.all()
		count = []
		good = []
		goodOfUser = []
		aboutGoods = []
		try:
			numOfOrder = str(orders[len(orders)-1].id)
		except Exception as e:
			numOfOrder = "1"
		
		for i in range(num):
			count.append(request.POST['count-'+str(i)])
			good.append(request.POST['good-'+str(i)])
			goodOfUser.append(Goods_of_user.objects.get(id = good[i]))
			aboutGoods.append(About_goods.objects.get(id = goodOfUser[i].goodId))
			aboutGoods[i].count -= int(count[i])
			if (aboutGoods[i].count < 0):
				return HttpResponseRedirect("/basket")
		for i in range(num):
			order = Orders(userName = goodOfUser[i].userName, goodId = goodOfUser[i].goodId, count = count[i], numberOfOrder = numOfOrder)
			aboutGoods[i].save();
			order.save()
			goodOfUser[i].delete()
	return HttpResponseRedirect("/basket")