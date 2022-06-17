from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from django.urls import reverse_lazy
from usedbikes .models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
from buyer.forms import Buyerprofileform,Buyerprofileupdateform
from buyer.models import Buyerprofile
class Buyerhomeview(TemplateView):
    template_name = "customers/buyer-home.html"

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



class Changepasswordview(TemplateView):
    template_name = "customers/changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")



        else:
            return render(request,self.template_name)


class Passwordresetview(TemplateView):
    template_name = "customers/passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')
        if pwd1!=pwd2:
            return render(request,self.template_name,{"mag":"incorrect password"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")



class Buyerprofileview(CreateView):
    model = Buyerprofile
    form_class = Buyerprofileform
    template_name = "customers/buyer-profile.html"
    success_url =reverse_lazy("buyer-home")
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class Buyerprofiledetailview(TemplateView):
     template_name = "customers/buyer-profileDETAILS.html"


class BuyerprofileEditview(FormView) :
    template_name = "customers/buyer-editprofile.html"
    form_class = Buyerprofileupdateform
    def get(self,request,*args,**kwargs):
        profile_details=Buyerprofile.objects.get(user=request.user)
        form=Buyerprofileupdateform(instance=profile_details,initial={"email":request.user.email,"phone":request.user.phone,"location":request.user.location})
        return  render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        profile_details=Buyerprofile.objects.get(user=request.user)
        form=self.form_class(instance=profile_details,data=request.POST,files=request.FILES)
        if form.is_valid():
            email=form.cleaned_data.pop("email")
            phone=form.cleaned_data.pop("phone")
            location=form.cleaned_data.pop("location")
            form.save()
            user=User.objects.get(id=request.user.id)
            user.email=email
            user.phone=phone
            user.location=location
            user.save()
            return redirect("buyer-home")
        else:
            return render(request.template_name,{"form":form})









