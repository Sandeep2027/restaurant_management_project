from django.shortcuts import render
from django.conf import settings
import requests


def get_base_context():
    return {
        "restaurant_name": settings.RESTAURANT_NAME
    }


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
    return render(request, "home/index.html", context)


def about_view(request):
    return render(request, "home/about.html", get_base_context())


def contact_view(request):
    return render(request, "home/contact.html", get_base_context())
