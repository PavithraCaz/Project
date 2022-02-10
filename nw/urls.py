from django.urls import path,include
from . import views

urlpatterns = [
  
    path('',views.Login,name="login"),
    path('User-Home',views.Home,name="home"),
]