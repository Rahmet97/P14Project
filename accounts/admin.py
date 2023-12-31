from django.contrib import admin
from .models import UserData


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'last_login')
    list_filter = ('username', 'first_name', 'last_name')
    list_editable = ('first_name', 'last_name', 'phone_number')
