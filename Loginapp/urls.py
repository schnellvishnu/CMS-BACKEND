from django.urls import path
from Loginapp import views
urlpatterns = [
   path("signin/",views.Loginview.as_view()) ,
   path("register/",views.Registerview.as_view()) , 
]
