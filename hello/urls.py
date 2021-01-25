from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("Sathwi",views.Sathwi,name="sathwi"),
    path("dhatri",views.dhatri,name="dhatri")
]