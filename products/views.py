from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from .models import Product, Item, MenuItem
from .serializers import ProductSerializer, ItemSerializer, MenuItemSerializer


# Item CRUD using ModelViewSet (replaces ItemView class)
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]


# Product ViewSet (read-only)
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


# MenuItem CRUD + custom menu view
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            return MenuItem.objects.filter(restaurant_id=restaurant_id)
        return super().get_queryset()

    @action(detail=False, methods=['get'])
    def menu_view(self, request):
        menu_items = MenuItem.objects.all()
        return render(request, 'products/menu.html', {'menu_items': menu_items})
