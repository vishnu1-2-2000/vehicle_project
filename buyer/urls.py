from buyer import views
from django.urls import path
urlpatterns = [
    path("home",views.Buyerhomeview.as_view(),name="buyer-home"),
    path("profile/add",views.Buyerprofileview.as_view(),name="buyer-profile"),
    path("profile/details",views.Buyerprofiledetailview.as_view(),name="buyer-profiledetail"),
    path("profile/edit",views.BuyerprofileEditview.as_view(),name="buyer-profileEDIT"),
    path("users/password/change",views.Changepasswordview.as_view(),name="password-change"),
    path("users/password/reset",views.Passwordresetview.as_view(),name="password-reset"),
    path("users/accounts/signout",views.signout_view,name="signout"),

]
