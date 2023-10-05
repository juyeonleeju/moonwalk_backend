
from django.contrib import admin
from .models import Account


from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
class AccounAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Account
<<<<<<< HEAD
    list_display = ('User_ID', 'email', 'password', 'name', 'phone')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Account, AccountAdmin)
=======
    list_display = ('User_ID','email','password','name','phone')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Account, AccounAdmin)
>>>>>>> bf3ddc0bc369481e26652f928ec407fba3fa9cc3


class Meta:
     model = AccounAdmin
     exclude = ('','')
    