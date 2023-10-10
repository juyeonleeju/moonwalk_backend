from django.db import models
from django.db.models import Sum

 
# Create your models here.
#운동기록

class Runrecord(models.Model): 
    walk_count = models.IntegerField(null=True,default =0) #하루 총 걸음 수
    calorie = models.IntegerField(null=True,default =0) #칼로리
    updated_at = models.DateTimeField(null=True,auto_now = True) #업데이트 날짜
    total_wc = models.IntegerField(null=True,default =0) #누적 총 걸음 수

    class Meta:
        db_table = "Runrecord"
  