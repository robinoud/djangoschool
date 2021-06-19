from os import name
from django.urls import path
from .views import HomePage, AboutPage, ContactUs

urlpatterns = [
    # localhost:8000/
    path('',HomePage, name = 'home-page'),
    path('about/', AboutPage, name='about-page'),
    path('contact/',ContactUs, name='contact-page')
]
