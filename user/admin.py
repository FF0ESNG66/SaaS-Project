from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm

    add_fieldsets = (
    ("Username", {
        'fields': ('username',),
    }),
    ("Personal information", {
        'fields': ('first_name', 'last_name', 'email', 'date_of_birth'),
    }),
    ("Password", {
        'fields': ('password1', 'password2')
    }),
)


admin.site.register(CustomUser, CustomUserAdmin)


# Observation:

# I'm importing and inheriting "UserAdmin" provided by Django for managing users in the admin panel

# I use the form that I've created in order to select the fields to display
# Inside of the tuple "add_fieldsets" I add those fields

# Then I register the CustomUser model with the CustomUserAdmin configuration enabling the admin panel to manage CustomUser instances using the customized admin interface.





# Structure of the "add_fieldsets":


# Outer Tuple: ( ... )

# This contains a single element, which is an single inner tuple or multiple tuples.



# Inner Tuple/s: (None/STR, { ... })

# The inner tuple contains two elements:
# The first element is used for specifying a legend or grouping (can be a string to label this section in the admin panel or set to None).
# The second element is a dictionary { ... }, defining the configuration for this fieldset.



# Dictionary:

# This specifies the fields to display in the admin panel when adding a new user. 
# Each field within the tuple will be displayed in the order provided.