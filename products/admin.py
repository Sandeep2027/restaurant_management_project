from django.contrib import admin
from .models import Product

class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']

admin.site.register(Item,ItemAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    ordering = ('name',)
    fields = ('name', 'description', 'price', 'created_at')
    readonly_fields = ('created_at',)
