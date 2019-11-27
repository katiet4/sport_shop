from django.db import models

class About_goods(models.Model):
    category = models.TextField()
    count = models.IntegerField()
    price = models.IntegerField()
    name = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.category


#categories:
    # games_with_balls

# class Goods_of_user(models.Model):
#     categories = models.TextField()
#     count = IntegerField()
#     price = IntegerField()
#     name = TextField();
#     def __str__(self):
#         return self.categories
