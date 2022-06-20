from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    stock = models.IntegerField(default=1)
