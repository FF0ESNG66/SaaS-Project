from django.contrib import admin
from .models import Course

@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'created_at', 'updated_at'] # This are the fields that will be displayed on the admin list display for Course objects
    search_fields = ['title', 'instructor__username'] # This will display a search bar and the fields named are the ones that can be use to search a course
    list_filter = ['created_at', 'updated_at', 'instructor'] # And this one allow us to filter Course objects based on specific criteria