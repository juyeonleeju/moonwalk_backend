from django.urls import path,include

from django.contrib import admin
from . import views


urlpatterns = [
    path('collections/', views.cRm_list),
]

