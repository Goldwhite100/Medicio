from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name