from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=254)
    ID = models.CharField(max_length = 500)
    password = models.CharField(max_length = 500)
    name = models.CharField(max_length = 500)
    phone = models.IntegerField(default=0,)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "Account"
