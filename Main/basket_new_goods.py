from Goods.models import Goods_of_user
def calculate_new(userName):
    result = 0
    try:
        goods = Goods_of_user.objects.filter(userName = userName)
        for i in goods:
            if(i.checked == 0):
                result+=1
        return result
    except Exception as e:
        return result
def confirm_check(userName):
    try:
        goods = Goods_of_user.objects.filter(userName = userName)
        for i in goods:
            i.checked = 1
            i.save()
        return 1
    except Exception as e:
        return 0
