from django.urls import path,include
from .views import course_list
from django.contrib import admin

from django.urls import path
from . import views



urlpatterns = [
    path('course_list/', views.course_list),
]

