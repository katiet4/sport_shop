from django.db import models

# Create your models here.
class Profile_of_user(models.Model):
    userId  =   models.IntegerField()#NEW
    userImg =   models.TextField(default = "images/avatar/no-ava.png")#NEW
    userStatus = models.TextField(default = "New Member")#NEW
    def __str__(self):
        return self.userId
