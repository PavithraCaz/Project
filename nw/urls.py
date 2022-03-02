from django.urls import path,include
from . import views

urlpatterns = [
  
    path('login/',views.Login,name="login"),
    path('',views.Home,name="home"),
    path('bs',views.Boot,name="boot"),
]