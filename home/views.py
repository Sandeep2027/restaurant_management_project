from django.shortcuts import render
from django.conf import settings
import requests
from restaurants.models import Restaurant
from django.http import HttpResponseServerError

def get_base_context():
    return {
        "restaurant_name": settings.RESTAURANT_NAME
    }

def get_restaurant_phone():
    restaurant = Restaurant.objects.first()
    if restaurant and hasattr(restaurant, 'phone_number'):
        return restaurant.phone_number
    return getattr(settings, 'RESTAURANT_PHONE', '')

def home(request):
    context = {
        'restaurant_name': request.settings.RESTAURANT_NAME
    }
    return render(request, 'home/index.html', context)

def about(request):
    context = {
        'restaurant_name': request.settings.RESTAURANT_NAME
    }
    return render(request, 'home/about.html', context)

def contact(request):
    context = {
        'restaurant_name': request.settings.RESTAURANT_NAME
    }
    return render(request, 'home/contact.html', context)

def reservations(request):
    context = {
        'restaurant_name': request.settings.RESTAURANT_NAME
    }
    return render(request, 'home/reservations.html', context)


def feedback(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment:
            Feedback.objects.create(comment=comment)
        return render(request, 'home/feedback.html', {'restaurant_name': request.settings.RESTAURANT_NAME, 'success': True})
    return render(request, 'home/feedback.html', {'restaurant_name': request.settings.RESTAURANT_NAME})
