from django.urls import path,include
from .views import cRm_list
from django.contrib import admin



urlpatterns = [
    path('/collections', cRm_list.as_view()),
]

