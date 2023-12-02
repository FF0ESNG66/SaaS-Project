from django.contrib.auth.models import UserManager
from django.utils import timezone

class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if extra_fields.get('date_of_birth') is None:
            extra_fields['date_of_birth'] = timezone.now() 

        return super().create_superuser(username, email, password, **extra_fields)
    

# Observation:

# Here I'm inheriting UserManeger class in order to modify the behavior of the "create_superuser" method.
# Whenever I override a superclass method, I must think:  - Do I want to replace this functionality entirely, or do I want to add to it? - 
# If I want to add to the functionality of the original method, I must either call the superclass method (using the super() syntax) 
# or be sure that you duplicate its behaviors.

# And by "duplicare its behavior" I mean that I should wirte then the lines:

# extra_fields.setdefault("is_staff", True)
# extra_fields.setdefault("is_superuser", True)