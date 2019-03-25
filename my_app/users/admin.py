
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import AdminUser, User


class AdminUserAdmin(UserAdmin):

    list_display = ('email', 'username', 'names', 'surnames')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        ('Autenticación',
            {'fields': ('id', 'email', 'username', 'password')}),
        ('Información personal',
            {'fields': ('names', 'surnames', 'gender', 'phone',)}),
        ('Información adicional',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Información adicional',
            {'fields': ('created_at', 'updated_at', 'last_login')}),
    )

    readonly_fields = ('id', 'created_at', 'updated_at', 'last_login')

    search_fields = ('email', 'surnames',)
    ordering = ('surnames', 'email')
    filter_horizontal = ()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'names', 'surnames')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        ('Autenticación',
            {'fields': ('id', 'email', 'username', 'password')}),
        ('Información personal',
            {'fields': ('names', 'surnames', 'gender', 'phone',)}),
        ('Información adicional',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Información adicional',
            {'fields': ('created_at', 'updated_at', 'last_login')}),
    )

    readonly_fields = ('id', 'created_at', 'updated_at', 'last_login')

    search_fields = ('email', 'surnames',)
    ordering = ('surnames', 'email')
    filter_horizontal = ()


admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(User, UserAdmin)
