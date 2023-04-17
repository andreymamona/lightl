from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_staff", "is_superuser",)
    fields = ("id", "email", "is_staff", "is_superuser",)
    readonly_fields = ("id",)
    search_fields = ("email",)



