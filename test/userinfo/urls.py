from django.urls import path,include
from .views import userinfoView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/userinfo', userinfoView.as_view()), 
    
] 