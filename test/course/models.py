
from django.db import models

class Runningmate(models.Model): 
    Rm_id = models.IntegerField(null=True,default =0)
    Rm_Name = models.CharField(null=True,max_length=200) #얘네는 필드임.
    Rm_color = models.CharField(null=True,max_length=200) 
    Rm_species = models.CharField(null=True,max_length=200)

    class Meta:
        db_table = "Runningmate"

  

#course = runningmate 