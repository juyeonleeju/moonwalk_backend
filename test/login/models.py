from django.db import models

# Create your models here.

class Account(models.Model):
    User_ID = models.CharField(null=True,max_length = 500)
    email = models.EmailField(null=True,max_length=254)
    password = models.CharField(null=True,max_length = 500)
    name = models.CharField(null=True,max_length = 500)
    phone = models.CharField(null=True,max_length = 11)
    created_at = models.DateTimeField(null=True,auto_now_add = True)
    updated_at = models.DateTimeField(null=True,auto_now = True)
    
    class Meta:
        db_table = "Account"


