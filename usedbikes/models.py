from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    options=(("seller","seller"),
             ("buyer","buyer"))
    role=models.CharField(max_length=120,choices=options,default="buyer")
    phone=models.CharField(max_length=12,null=True)
    location=models.CharField(max_length=120)











class Bikes(models.Model):
    bike_name=models.CharField(max_length=150)
    company=models.ForeignKey(User,on_delete=models.CASCADE,related_name="company")
    location=models.CharField(max_length=120)
    model=models.PositiveIntegerField(null=True)


    killometer_run=models.PositiveIntegerField(null=True)
    price=models.PositiveIntegerField(default=0)
    created_date=models.DateField(auto_now_add=True)
    active_status=models.BooleanField(default=True)




def __init__(self):
    return self.bike_name




class Bikeprofile(models.Model):
    seller=models.CharField(max_length=120)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="usedbikes")
    location=models.CharField(max_length=120)
    phone_number=models.PositiveIntegerField(default=0)
    profile_photo=models.ImageField(upload_to="bikeprofile",null=True)

    