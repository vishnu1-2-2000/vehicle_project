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
    path("bike/all",views.Buyervehiclelistview.as_view(),name="bike-list"),
    path("bike/info/<int:id>",views.BuyervehicleDetailview.as_view(),name="bike-info"),
    path("bike/buy-now/<int:id>",views.buy_now,name="buynow"),
    path("application/all",views.BuyervehicleApplicationListview.as_view(),name="buyer-application"),
    path("application/remove/<int:id>",views.cancell_vehicle,name="buyer-cancel")

]
