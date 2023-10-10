
from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

from django.contrib import admin
from .models import collections

# Register your models here.
class collectionsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = collections
    list_display = ('cRm_id', 'cRm_Name', 'cRm_color', 'cRm_species', )
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( collections, collections)


class Meta:
     model = collectionsAdmin
     exclude = ('','')
    
