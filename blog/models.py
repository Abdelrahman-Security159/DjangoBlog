from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=150, blank=True)
    body = models.TextField(max_length=5000)
    auther = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title} : {self.auther}"