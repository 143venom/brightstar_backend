from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(UA):
    list_display = (
        "email",
        "username",
    )

    search_fields = (
        "email",
        "username",
    )

    list_per_page = 10
