from django.db import models

# Create your models here.
class order(models.Model):
    iteam = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=5)
    quantity = models.CharField(max_length=5)
    date = models.DateField()
