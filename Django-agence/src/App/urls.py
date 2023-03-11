from django.urls import path

from .views import home, Connexion, register, deconnection, contact, confimation

urlpatterns = [

    path('home/', home, name="home"),
    path('login/', Connexion, name="login"),
    path('register/', register, name="register"),
    path('logout/', deconnection, name="logout"),
    path('contact/', contact, name="contact"),
    path('confirmation/', confimation, name="confirmation"),

]
