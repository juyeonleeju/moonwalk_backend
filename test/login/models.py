from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.CharField(max_length = 200)
    ID = models.CharField(max_length = 500)
    password = models.CharField(max_length = 500)
    name = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

   