from django.contrib import admin
from django.urls import path, include

from course.views import course_list
			

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.views')),
    #path("<int:id>/",course_list)
]


