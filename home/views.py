from django.shortcuts import render
from django.conf import settings
import requests
from restaurants.models import Restaurant

def get_base_context():
    return {
        "restaurant_name": settings.RESTAURANT_NAME
    }

def get_restaurant_phone():
    restaurant = Restaurant.objects.first()
    if restaurant and hasattr(restaurant, 'phone_number'):
        return restaurant.phone_number
    return getattr(settings, 'RESTAURANT_PHONE', '')

def home_view(request):
    api_url = f"{settings.SITE_URL}/api/products/"
    products = []
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        products = response.json()
    except requests.RequestException:
        pass

    context = get_base_context()
    context["products"] = products
    context["phone_number"] = get_restaurant_phone()
    return render(request, "home/index.html", context)

def about_view(request):
    context = get_base_context()
    return render(request, "home/about.html", context)

def contact_view(request):
    context = get_base_context()
    return render(request, "home/contact.html", context)
