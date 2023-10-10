
from django.db import models

# Create your models here.
class userinformation(models.Model):
     nickname = models.CharField(null=True,max_length = 8) #닉네임
     residence =  models.CharField(null=True,max_length = 20) #거주지역
     goal = models.CharField(null=True,max_length=100) #운동목적?
     weight = models.IntegerField(null = True, default = 40)
     attendance = models.DateField(null=True,auto_now = True) #출석일수
   
     class Meta:
        db_table = "userinfo"

        #이거 모델에 맞게 바꾸기
