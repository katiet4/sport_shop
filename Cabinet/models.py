from django.db import models

# Create your models here.
class Orders(models.Model):
    userName =  models.TextField()
    goodId  =   models.IntegerField()
    count = models.IntegerField()
    numberOfOrder = models.TextField()
    status = models.TextField(default = "Отправлено")
    def __str__(self):
        return self.numberOfOrder
