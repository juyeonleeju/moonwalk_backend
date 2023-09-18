from django.urls import path,include
from .views import Rm_list
from django.contrib import admin



urlpatterns = [
    path('/RunningMate', Rm_list.as_view()),
]

