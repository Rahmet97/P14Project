from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

