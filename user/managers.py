from django.contrib.auth.models import UserManager
from django.utils import timezone

class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('date_of_birth') is None:
            extra_fields['date_of_birth'] = timezone.now() 

        return self._create_user(username, email, password, **extra_fields)
    
    