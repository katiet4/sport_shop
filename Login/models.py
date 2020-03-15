from django.db import models

# Create your models here.
class Profile_of_user(models.Model):
    userId  =   models.IntegerField()
    userImg =   models.TextField(default = "images/avatar/no-ava.png")
    userStatus = models.TextField(default = "New Member")
    def __str__(self):
        return self.userId
