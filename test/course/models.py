from django.db import models

class Course(models.Model): 
    ESNTL_ID = models.CharField(null=True,max_length=200) #얘네는 필드임.
    WLK_COURS_FLAG_NM = models.CharField(null=True,max_length=200) 
    WLK_COURS_NM = models.CharField(null=True,max_length=200)
    COURS_DC =models.TextField(null=True)
    SIGNGU_NM = models.CharField(null=True,max_length=200)
    COURS_LEVEL_NM = models.CharField(null=True,max_length=200)
    COURS_DETAIL_LT_CN = models.IntegerField(default=0) #32bit정수
    ADIT_DC = models.TextField(null=True)
    COURS_TIME_CN = models.CharField(null=True,max_length=200)
    TOILET_DC = models.CharField(null=True,max_length=200)
    LNM_ADDR = models.CharField(null=True,max_length=200)
    COURS_SPOT_LA = models.FloatField(null=True,max_length=200) #소수점
    COURS_SPOT_LO = models.FloatField(null=True,max_length=200) #소수점

def __str__(self):
        return self.title #객체 문자열 표현 리턴 


