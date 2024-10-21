from django.db import models

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=50)  # başlık
    author = models.CharField(max_length=50)  # yazar
    isbn= models.CharField(max_length=50)  
    
    def __str__(self):
        return f"{self.tile} {self.author}"