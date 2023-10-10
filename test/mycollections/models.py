from django.db import models

# Create your models here.
class collections(models.Model):
    cRm_id = models.IntegerField(null=True,default =0)
    cRm_Name = models.CharField(null=True,max_length=200) #얘네는 필드임.
    cRm_color = models.CharField(null=True,max_length=200) 
    cRm_species = models.CharField(null=True,max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    db_table = "my_collections"
