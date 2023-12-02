from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path("", views.course_list_view, name="course-list"),
    path("<int:course_id>/", views.course_detail_view, name="course-detail"),
]