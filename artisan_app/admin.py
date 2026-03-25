from django.contrib import admin
from .models import UserProfile, Listing


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'impressions', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
