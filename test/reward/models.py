from django.db import models

# Create your models here.

class reward(models.Model):
    ID = models.CharField(max_length = 500)
    fuel = models.CharField(max_length = 500)
    name = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
