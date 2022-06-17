from django.db import models
from usedbikes.models import User
# Create your models here.


class Buyerprofile(models.Model):
    profile_photo=models.ImageField(upload_to="buyerprofile")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="buyer")
    buyer=models.CharField(max_length=150)
    location=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=120)

