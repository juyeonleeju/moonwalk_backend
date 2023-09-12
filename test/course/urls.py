from django.urls import path,include
from .views import course_list
from django.contrib import admin



urlpatterns = [
    path('/course', course_list.as_view()),
]

