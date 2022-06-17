from django import forms
from buyer.models import Buyerprofile


class Buyerprofileform(forms.ModelForm):
    class Meta:
        model=Buyerprofile
        exclude=("user",)


class Buyerprofileupdateform(forms.ModelForm):
    email=forms.CharField()
    phone=forms.CharField()
    location=forms.CharField()
    class Meta:
        model=Buyerprofile
        fields=["email","phone","location","buyer","profile_photo"]

