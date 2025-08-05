from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone_number')
    search_fields = ('user__username', 'name', 'email', 'phone_number')
    readonly_fields = ('user',)
