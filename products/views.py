from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view

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

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'products/menu.html', {'menu_items': menu_items})

@api_view(['POST'])
def create_menu_item(request):
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_menu_items(request):
    restaurant_id = request.query_params.get('restaurant_id')
    if restaurant_id:
        try:
            menu_items = MenuItem.objects.filter(restaurant_id=restaurant_id)
        except ValueError:
            return Response({"error": "Invalid restaurant_id"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        menu_items = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_menu_item(request, pk):
    try:
        menu_item = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)
    except MenuItem.DoesNotExist:
        return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_menu_item(request, pk):
    try:
        menu_item = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except MenuItem.DoesNotExist:
        return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_menu_item(request, pk):
    try:
        menu_item = MenuItem.objects.get(pk=pk)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except MenuItem.DoesNotExist:
        return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
