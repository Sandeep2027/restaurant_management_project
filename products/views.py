from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from .models import Product, Item, MenuItem
from .serializers import ProductSerializer, ItemSerializer, MenuItemSerializer


# Item APIView
class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product ViewSet (readonly)
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


# Menu View with CRUD using ViewSet
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
        # Hardcoded menu items for now (can be replaced with DB query later)
        menu_items = [
            {"name": "Paneer Butter Masala", "description": "Creamy paneer dish with rich tomato sauce", "price": 12.99, "is_available": True},
            {"name": "Margherita Pizza", "description": "Classic pizza with mozzarella and basil", "price": 10.99, "is_available": True},
            {"name": "Chocolate Lava Cake", "description": "Warm cake with a molten chocolate center", "price": 5.99, "is_available": False},
        ]
        return render(request, 'products/menu.html', {'menu_items': menu_items})
