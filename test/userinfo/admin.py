
from django.contrib import admin
from .models import User_info

# Register your models here.
class User_infoAdmin(admin.ModelAdmin):
    resource_class = User_info
    list_display = ('nickname','residence')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( User_info, User_infoAdmin)   

class Meta:
     model = User_infoAdmin
     exclude = ('','')
    