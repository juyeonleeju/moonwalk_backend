# from django.urls import path,include
# from .views import SignUpView, SignInView
# from django.contrib import admin

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('/up', SignUpView.as_view()), 
#     path('/in', SignInView.as_view()),
# ] 

from django.urls import include, path
from . import views

login_patterns = [
    path('normal/', views.login, name='login'),
]

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', include(login_patterns)),
]