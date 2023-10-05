from django.urls import path,include
<<<<<<< HEAD
from .views import userinfoView
=======
from .views import User_info
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('/userinfo', userinfoView.as_view()), 
=======
    path('/userinfo', User_info.as_view()), 
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3
    
] 