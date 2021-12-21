from django.db import models


class Author(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.user_name} : ({self.first_name} {self.last_name})"
    