from django import forms
from usedbikes.models import Bikes,Bikeprofile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Bikesform(forms.ModelForm):
    class Meta:
        model=Bikes
        fields="__all__"
        

class Signupform(UserCreationForm) :
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)



class Passwordresetform(forms.Form):
    password1=forms.CharField(widget=forms.PasswordInput)
    confirm_passwor=forms.CharField()
    def clean(self):
        cleane_data=super().clean()
        pwd1=cleane_data.get("password1")
        pwd2=cleane_data.get("conform_password")
        if pwd1!=pwd2:
            msg="password miss match"
            self.add_error("password1",msg)


class Bikeprofileform(forms.ModelForm):
    class Meta:
        model=Bikeprofile
        exclude=("user",)




















