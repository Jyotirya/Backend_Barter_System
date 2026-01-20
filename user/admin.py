from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CreateUserForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "is_staff",
        "is_active",
    ]
    ordering = ("email",)
    search_fields = ("email",)

    fieldsets = [
        (None, {"fields": ("email", "password")}),
        ("Personal info", 
            {"fields": [
                "first_name",
                "last_name",
                "address1",
                "address2",
            ]}
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    ]

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin) # For user creation