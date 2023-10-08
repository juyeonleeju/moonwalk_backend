from django.contrib import admin
from django.urls import path, include

#from course.views import course_list
	
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('login.urls')), #login앱
]

