from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("summerScoop", views.summerScoop, name="summerScoop"),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('signIn', views.signIn, name='signIn'),
    path("signUp", views.signUp, name="signUp"),
]
