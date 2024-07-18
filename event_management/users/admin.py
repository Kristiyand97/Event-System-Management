# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Customize UserAdmin if needed
class CustomUserAdmin(UserAdmin):
    model = User
    # Add any custom configuration here
    # For example, you can define fieldsets, add filter options, etc.
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
