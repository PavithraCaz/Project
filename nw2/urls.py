from django.urls import path,include
from . import views

urlpatterns = [
    path('mod',views.Md),
]