# Register your models here.

from django.contrib import admin
from .models import Runningmate

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

from django.contrib import admin
from .models import Runningmate

# Register your models here.
class RunningmateAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Runningmate
    list_display = ('Rm_id', 'Rm_Name', 'Rm_color', 'Rm_species', )
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Runningmate, RunningmateAdmin)


class Meta:
     model = RunningmateAdmin
     exclude = ('','')
    
