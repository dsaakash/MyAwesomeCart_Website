from . import views
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path("", views.index,name="ShopHome"),
]
