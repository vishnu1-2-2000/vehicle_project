from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bikes(models.Model):
    bike_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=120)
    model=models.PositiveIntegerField(null=True)


    killometer_run=models.PositiveIntegerField(null=True)
    price=models.PositiveIntegerField(default=0)




def __init__(self):
    return self.bike_name




class Bikeprofile(models.Model):
    bikename=models.CharField(max_length=120)
    company_name=models.CharField(max_length=120)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="usedbikes")
    location=models.CharField(max_length=120)
    model=models.PositiveIntegerField(null=True)
    logo=models.ImageField(upload_to="bikeprofile",null=True)

    