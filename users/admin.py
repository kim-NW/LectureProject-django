from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profle",
            {
                "fields": (
                    "username",
                    "password",
                    "nickname",
                    "email",
                    "name",
                    "dateBirth",
                    "gender",
                    "phoneNumber",
                    "profileImg",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "isInstructor",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "is_staff",
                ),
                "classes": ("collapse",),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "name", "is_staff")
