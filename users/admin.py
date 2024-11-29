from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    list_display = ["username", "first_name", "last_name", "email", "is_active"]
    list_filter = ["is_active", "user_type"]
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username", )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "followed")
    search_fields = ("follower__username", "followed__username")


admin.site.register(User, CustomUserAdmin)
admin.site.register(Follow, FollowAdmin)