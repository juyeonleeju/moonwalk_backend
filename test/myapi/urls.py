
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
    #path('sign/', include('account.urls')),
    
]

