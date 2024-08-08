from django.urls import path
from .views import home, about, services, contact, profile

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile'),
]
