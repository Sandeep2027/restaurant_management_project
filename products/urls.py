from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('', include(router.urls)),

]



