from django.contrib import admin
from usedbikes import views
from django.urls import path
urlpatterns = [
path("home",views.Usedbikesview.as_view(),name="bike-home"),
path("bikes/add",views.Addvehicleview.as_view(),name="bikes-add"),
path("bikes/list",views.Listvehicleview.as_view(),name="bikes-list"),
path("bikes/details/<int:id>",views.Detailview.as_view(),name="details"),
path("bikes/edit/<int:id>",views.Editvehicleview.as_view(),name="bikes-edit"),
path("bikes/delete/<int:id>",views.Deletevehicleview.as_view(),name="bikes-delete"),
path("users/accounts/signup",views.Signupview.as_view(),name="signup"),
path("users/accounts/signin",views.Signinview.as_view(),name="signin"),
path("users/accounts/signout",views.signout_view,name="signout"),
path("users/password/change",views.Changepasswordview.as_view(),name="password-change"),
path("users/password/reset",views.Passwordresetview.as_view(),name="password-reset"),
path("profile/add",views.Bikeprofileview.as_view(),name="bikes-addprofile"),
path("profile/detail",views.Bikeviewprofileview.as_view(),name="bikes-profile"),
path("profile/edit/<int:id>",views.BikeprofileEditView.as_view(),name="bike-editprofile"),
path("application/all/<int:id>",views.VehiclelistApplications.as_view(),name="veh-applist"),
path("application/details/all/<int:id>",views.VehicleApplicationDetailView.as_view(),name="veh-detail"),
path("bike/application/status/change/<int:id>",views.reject_application,name="rej-appl")


]
