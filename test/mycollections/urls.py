from django.urls import path,include
from . import views
from django.contrib import admin



urlpatterns = [
    path('collectionget/', views.collectionsAPIView.as_view()),
    path('collectionput/', views.cRm_listAPIView.as_view()),
]