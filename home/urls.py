from django.urls import path
from  .views import home, about, contact,  reservations

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
  path('reservations/', reservations, name='reservations'),
     path('feedback/', feedback, name='feedback'),
]
