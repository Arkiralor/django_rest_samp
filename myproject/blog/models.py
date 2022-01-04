from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    body = models.CharField(max_length=2048)
    email = models.EmailField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

