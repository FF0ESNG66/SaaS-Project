from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    date_of_birth = models.DateField()

    objects = CustomUserManager()


    class Meta:
        verbose_name = "customuser"
        verbose_name_plural = "customusers"
        db_table = "customuser"


    def __str__(self) -> str:
        return self.username
    


# Observation

# " objects = CustomUserManager() "

# By default every model has a manager that is an interface through which database query operations are provided to Django models.
# The default "User" model provided by Django use the "UserManager" as a manager by default

# Since I've created a custom User model (CustomUser) and I've changed some fields such as making the email required (null=False) and adding "date_of_birth"
# I had to also create a custom manager (CustomUserManager) to handle "date_of_birth" because, whenever I create a superuser using
# "py manage.py createsuperuser" it won't ask me for a date of birth and that field is required (null=False by default in Django) resulting in an error

# So after handling that in my CustomUserManager I set that manager as the default manager in my CustomUser using the variable "objects"