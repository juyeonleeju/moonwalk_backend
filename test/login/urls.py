from django.urls import path,include
from .views import SignUpView, SignInView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/up', SignUpView.as_view()), 
    path('/in', SignInView.as_view()),
] 