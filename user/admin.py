from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm

    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

