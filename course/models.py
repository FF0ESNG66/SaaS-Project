from django.db import models
from user.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="courses_taught")
    subscribers = models.ManyToManyField(CustomUser, related_name="courses_subscribed", blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.00)


    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"
        db_table = "course"


    def __str__(self) -> str:
        return self.title