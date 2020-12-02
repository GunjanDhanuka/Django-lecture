from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gunjan", views.gunjan, name="gunjan"),
    path("niyati", views.niyati, name="niyati"),
    path("<str:name>", views.greet, name="greet")
]