from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView,TemplateView
from usedbikes.forms import Bikesform,Signupform,Loginform,Passwordresetform,Bikeprofileform
from usedbikes.models import Bikes,Bikeprofile
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class Usedbikesview(View):
    def get(self,request):
        return render(request,"home.html")




class Addvehicleview(CreateView):
    model = Bikes
    form_class = Bikesform
    template_name = "bikes-add.html"
    success_url = reverse_lazy("bikes-list")
    # def get(self,request):
    #     form=Bikesform()
    #     return render(request,"bikes-add.html",{"form":form})
    #
    # def post(self,request):
    #     form=Bikesform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"home.html")
    #     else:
    #         return render(request,"bikes-add.html",{"form":form})



class Listvehicleview(ListView):
    model=Bikes
    context_object_name = "bikes"
    template_name = "bikes-list.html"


class Detailview(View):
    def get(self,request,id):
        qs=Bikes.objects.get(id=id)
        return render(request,"bikes-detail.html",{"bikes":qs})
    # model=Bikes
    # context_object_name = "bikes"
    # template_name = "bikes-detail.html"
    # pk_url_kwarg = "id"


class Editvehicleview(UpdateView):
    model = Bikes
    form_class = Bikesform
    template_name = "bikes-edit.html"
    success_url = reverse_lazy("bikes-list")
    pk_url_kwarg = "id"


class Deletevehicleview(DeleteView) :
    template_name = "bikes-delete.html"
    success_url = reverse_lazy("bikes-list")
    pk_url_kwarg = "id"
    model = Bikes




class Signupview(CreateView) :
    model = User
    form_class = Signupform
    template_name = "usersignup.html"
    success_url = reverse_lazy("bikes-list")



class Signinview(FormView):
    form_class = Loginform
    template_name = "login.html"
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("bikes-list")
            else:
                return render(request,"login.html",{"form":form})



def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



class Changepasswordview(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")



        else:
            return render(request,self.template_name)


class Passwordresetview(TemplateView):
    template_name = "passwordreset.html"
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



class Bikeprofileview(CreateView):
    model=Bikeprofile
    form_class = Bikeprofileform
    template_name = "bikes-addprofile.html"
    success_url = reverse_lazy("bike-home")


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
class Bikeviewprofileview(TemplateView):
    template_name = "bike-profile.html"



class BikeprofileEditView(UpdateView):
    model=Bikeprofile
    form_class = Bikeprofileform
    template_name = "bike-editprofile.html"
    success_url = reverse_lazy('bikes-profile')
    pk_url_kwarg = "id"






















