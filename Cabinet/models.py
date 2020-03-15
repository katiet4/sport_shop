from django.db import models

# Create your models here.
class Orders(models.Model):
    userName =  models.TextField()
    goodId  =   models.IntegerField()
    count = models.IntegerField()
    result = models.IntegerField(default = 0)
    numberOfOrder = models.TextField()
    status = models.TextField(default = "Отправлено")
    def __str__(self):
        return self.numberOfOrder

class Comments(models.Model):
    goodId =  models.IntegerField()
    userId  =   models.IntegerField()
    comment  =   models.TextField()
    rating  =   models.IntegerField(default = 0)
    def __str__(self):
        return str(self.goodId)
