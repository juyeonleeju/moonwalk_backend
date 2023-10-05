
from django.contrib import admin
<<<<<<< HEAD
from .models import userinformation

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
class userinfoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = userinformation
    list_display = ('nickname', 'residence', 'goal', 'weight', )
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( userinformation, userinfoAdmin)


class Meta:
     model = userinfoAdmin
     exclude = ('','')
    
=======
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
    
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3
