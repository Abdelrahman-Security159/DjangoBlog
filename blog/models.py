from django.db import models
from django.db.models.deletion import PROTECT
from author.models import Author

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=150)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return f"{self.title} : {self.author}"