from django.db import models

class About_goods(models.Model):
    rating = models.IntegerField(default = 0)#NEW




    category = models.TextField()
    count = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(default = "description empty")
    name = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.category


#categories:
    # games_with_balls

class Goods_of_user(models.Model):
    userName =  models.TextField()
    goodId  =   models.IntegerField()
    def __str__(self):
        return self.userName



class Comments(models.Model):
    goodId =  models.IntegerField()#NEW
    userId  =   models.IntegerField()#NEW
    comment  =   models.TextField()#NEW
    rating  =   models.IntegerField()#NEW
    def __str__(self):
        return self.userName
