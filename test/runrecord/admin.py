

# Register your models here.

from django.contrib import admin
from .models import Runrecord


from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
class RunrecordAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Runrecord
    list_display = ('walk_count', 'calorie')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Runrecord, RunrecordAdmin)


class Meta:
     model = RunrecordAdmin
     exclude = ('','')
    