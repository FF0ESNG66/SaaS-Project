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


# Observation:

# I'm importing and inheriting "UserAdmin" provided by Django for managing users in the admin panel

# I use the form that I've created in order to select the fields to display
# Inside of the tuple "add_fieldsets" I add those fields

# Then I register the CustomUser model with the CustomUserAdmin configuration enabling the admin panel to manage CustomUser instances using the customized admin interface.

