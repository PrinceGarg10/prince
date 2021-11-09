from django.db import models

# Create your models here.
class order(models.Model):
    iteam = models.CharField(max_length=20,null=True)
    price = models.CharField(max_length=5,null=True)
    quantity = models.CharField(max_length=5,null=True)
    date = models.DateField(null=True)
    email = models.CharField(max_length=60,null= True)
    desc = models.TextField(null=True)

