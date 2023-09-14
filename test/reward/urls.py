
from django.urls import path,include
from .views import Reward
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/reward', Reward.as_view()), 
    
] 

