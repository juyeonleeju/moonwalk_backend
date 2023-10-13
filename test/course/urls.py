from django.urls import path,include
from .views import RandomRunningmateView
from django.contrib import admin



urlpatterns = [
    path('/RunningMate', RandomRunningmateView.as_view()),
]

