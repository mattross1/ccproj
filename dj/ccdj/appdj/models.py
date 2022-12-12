from django.db import models

# Create your models here.
class Food(models.Model):
    entry = models.IntegerField()
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    favorite = models.CharField(max_length=50)