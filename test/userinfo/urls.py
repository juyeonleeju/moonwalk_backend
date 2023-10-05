from django.urls import path,include
from .views import User_info
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/userinfo', User_info.as_view()), 
    
] 