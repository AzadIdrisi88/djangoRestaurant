from django.urls import path
from . import views

urlpatterns = [
 path('',views.index),
 path('registration/',views.registration),
 path('login/',views.dologin), 
 path('home/',views.home),
 path('logout/',views.logout),
 path('book/',views.create),
 path('search/',views.search),
 path('delete/',views.delete),
 path('weather/',views.weather),
 path('swapi/',views.swapi),
 path('update/',views.update),
 path('people/',views.people),
 path('movie/',views.movie),
 path('city/',views.getWeather),
 path('find/',views.getwdata),
]