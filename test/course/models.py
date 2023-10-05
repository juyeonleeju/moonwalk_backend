from django.db import models

class Runningmate(models.Model): 
    Rm_id = models.IntegerField(null=True,default =0)
    Rm_Name = models.CharField(null=True,max_length=200) #얘네는 필드임.
    Rm_color = models.CharField(null=True,max_length=200) 
<<<<<<< HEAD
    Rm_specise = models.CharField(null=True,max_length=200)
=======
    Rm_species = models.CharField(null=True,max_length=200)
    Rm_level = models.IntegerField(null=True,default =0)
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3

    class Meta:
        db_table = "Runningmate"

<<<<<<< HEAD
  
=======
    
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3

#course = runningmate 