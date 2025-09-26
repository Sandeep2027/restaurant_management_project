from django.shortcuts import render
from restaurants.models import Restaurant
from django.http import HttpResponseServerError
from .models import Feedback, ContactSubmission

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            ContactSubmission.objects.create(name=name, email=email)
    try:
        restaurant = Restaurant.objects.first()
        context = {
            'restaurant_name': request.settings.RESTAURANT_NAME,
            'phone_number': restaurant.phone_number if restaurant else request.settings.RESTAURANT_PHONE,
            'address': f"{restaurant.address}, {restaurant.city}" if restaurant else "123 Flavor Street, Foodville"
        }
        return render(request, 'home/index.html', context)
    except Exception as e:
        return HttpResponseServerError("An error occurred. Please try again later.")

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
