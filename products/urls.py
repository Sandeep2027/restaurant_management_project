from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import ProductViewSet
from .views import create_menu_item, list_menu_items, get_menu_item, update_menu_item, delete_menu_item, menu_view
router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('', include(router.urls)),
      path('menu-items/', list_menu_items, name='list_menu_items'),
    path('menu-items/create/', create_menu_item, name='create_menu_item'),
    path('menu-items/<int:pk>/', get_menu_item, name='get_menu_item'),
    path('menu-items/<int:pk>/update/', update_menu_item, name='update_menu_item'),
    path('menu-items/<int:pk>/delete/', delete_menu_item, name='delete_menu_item'),
    path('menu/', menu_view, name='menu_view'),

]







