from django.shortcuts import render
import requests
from django.conf import settings

def home_view(request):
    api_url = f"{settings.SITE_URL}/api/products/"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        products = response.json()
    except requests.RequestException:
        products = []
    return render(request, 'home/index.html', {'products': products})


def about_view(request):
    return render(request, 'home/about.html', {
        'restaurant_name': settings.RESTAURANT_NAME
    })
