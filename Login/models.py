from django.db import models
# Create your models here.
class Profile_of_user(models.Model):
    userId  =   models.IntegerField(default = 1)
    userImg =   models.ImageField(default = "/static/media/images/avatar/no-ava.png", upload_to = "static/media/images/avatar")
    userStatus = models.TextField(default = "New Member")
    def __str__(self):
        return str(self.userId)
        
class URL_for_reset(models.Model):
    codeURL  =   models.TextField()
    userId =   models.IntegerField(default = 1)
    def __str__(self):
        return self.codeURL
