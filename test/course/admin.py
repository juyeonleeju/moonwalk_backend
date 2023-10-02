from django.contrib import admin
from .models import Runningmate

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

class RmAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Runningmate
    list_display = ('Rm_Name', 'Rm_color', 'Rm_species',)
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Runningmate, RmAdmin)   


class RmInfoResource(resources.ModelResource):
    WLK_COURS_FLAG_NM = fields.Field(
        column_name = 'Rm_Name', attribute='Rm_Name',
        widget=ForeignKeyWidget(Runningmate,'Rm_Name')
    )
#어디서 찾아서 복붙한건데 무슨 문법인지 모르겟ㅠㅜ

class Meta:
     model = RmInfoResource
     exclude = ('','')