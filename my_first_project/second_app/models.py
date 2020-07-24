from django.db import models

# Create your models here.
class My_Model(models.Model):
    Product_Name=models.CharField(max_length=100)
    Product_company=models.CharField(max_length=100)
    Original_Price=models.FloatField()
    MRP=models.FloatField()

    def __str__(self):
        return self.Product_Name