from django.db import models

# Create your models here.
class profile(models.Model):
    Product_Name=models.CharField(max_length=100)
    Product_Price=models.FloatField()

    def __str__(self):
        return self.Product_Name