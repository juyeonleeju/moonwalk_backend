from django.db import models

# Create your models here.
#운동기록
class Runrecord(models.Model): 
    walk_count = models.IntegerField(null=True,default =0)
    calorie = models.IntegerField(null=True,default =0) #얘네는 필드임.
    created_at = models.DateTimeField(null=True,auto_now_add = True)
    updated_at = models.DateTimeField(null=True,auto_now = True)
    
    db_table = "Runrecord"
