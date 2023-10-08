from django.db import models

# Create your models here.

class Reward(models.Model): #리워드 보상
    xp = models.IntegerField(null=True,default = 0 ) #하루 운동량(걸음수)
    User_lev = models.IntegerField(null=True,default = 0) #레벨
    created_at = models.DateTimeField(null=True,auto_now_add = True)
    updated_at = models.DateTimeField(null=True,auto_now = True) #업데이트날짜

    class Meta:
        db_table = "Rewards"