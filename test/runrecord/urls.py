from django.urls import path,include
from .views import RunrecordView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/Runrecordinfo', RunrecordView.as_view()), 
    
] 