from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "email", "role", "is_staff", "is_active",)
    list_filter = ("username", "email", "role", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "role", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "role", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username", "email",)
    ordering = ("username", "email", "role")


admin.site.register(User, UserAdmin)