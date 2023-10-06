from django.db import models

# Create your models here.
#운동기록

class Runrecord(models.Model): 
    walk_count = models.IntegerField(null=True,default =0) #걸음 수
    calorie = models.IntegerField(null=True,default =0) #칼로리
    updated_at = models.DateTimeField(null=True,auto_now = True) #업데이트 날짜
    
    db_table = "Runrecord"
