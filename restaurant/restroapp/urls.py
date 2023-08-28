from django.urls import path
from . import views

urlpatterns = [
 path('',views.index),
 path('registration/',views.registration),
 path('login/',views.dologin), 
 path('home/',views.home),
 path('logout/',views.logout),
]