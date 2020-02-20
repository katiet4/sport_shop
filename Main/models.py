from django.db import models


class News(models.Model):
    category = models.TextField()
    title = models.TextField()
    text = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
