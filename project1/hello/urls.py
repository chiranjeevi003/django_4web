from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    #path("<str:name>",views.greet,name="greet"),
    path("chp5", views.chp5, name="chp5"), # hello/chp5
    path("harshu", views.harshu, name="harshu") # comes after hello/harshu

]