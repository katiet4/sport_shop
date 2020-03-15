from django.db import models
# Create your models here.
class Profile_of_user(models.Model):
    userId  =   models.IntegerField(default = 1)
    userImg =   models.FileField(default = "/static/media/images/avatar/no-ava.png")
    userStatus = models.TextField(default = "New Member")
    def __str__(self):
        return str(self.userId)
