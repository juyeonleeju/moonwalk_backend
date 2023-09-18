from django.db import models

# Create your models here.

class Reward(models.Model): #리워드 보상
    xp = models.IntegerField(default = 0) #경험치
    COURS_LEVEL_NM = models.CharField(null=True,max_length=200)
    #User_ID = models.ForeignKey(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "Reward"
        
