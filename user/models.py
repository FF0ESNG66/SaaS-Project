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
    

