<<<<<<< HEAD

from django.db import models

# Create your models here.
class userinformation(models.Model):
     nickname = models.CharField(null=True,max_length = 500) #닉네임
     #img = models.ImageField(null=True,upload_to='images/') #프로필사진
=======
from django.db import models

# Create your models here.
class User_info(models.Model):
     User_ID = models.ForeignKey('login.Account', on_delete=models.CASCADE, db_column='User_ID',default = 0)
     nickname = models.CharField(null=True,max_length = 500) #닉네임
     img = models.ImageField(null=True,upload_to='images/') #프로필사진
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3
     residence =  models.CharField(null=True,max_length = 500) #거주지역
     goal = models.CharField(null=True,max_length=100) #운동목적?
     weight = models.IntegerField(null = True, default = 40)
     attendance = models.DateField(null=True,auto_now = True) #출석일수
   
<<<<<<< HEAD
     class Meta:
        db_table = "userinfo_userinformation"

        #이거 모델에 맞게 바꾸기
=======
class Meta:
        db_table = "User_info"




>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3
