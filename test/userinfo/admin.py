
from django.contrib import admin
from .models import userinformation

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

from django.contrib import admin
from .models import Runrecord

# Register your models here.
class userinfoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = userinformation
    list_display = ('nickname', 'Rm_Name', 'Rm_color', 'Rm_species', )
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( userinformation, userinfoAdmin)


class Meta:
     model = userinfoAdmin
     exclude = ('','')
    
