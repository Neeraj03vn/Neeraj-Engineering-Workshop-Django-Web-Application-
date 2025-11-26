from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpage),
    path('home', views.home),
    path('services', views.services),
    path('about', views.about),
    path('contact', views.contact),
    path('truss', views.truss),

]
