from django.contrib import admin
from django.contrib import admin
from .models import Account

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
class AccountAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Account
    list_display = ('email','ID','password','name','phone')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Account, AccountAdmin)   
#admin.site.register(Course)

class CourseInfoResource(resources.ModelResource):
    WLK_COURS_FLAG_NM = fields.Field(
        column_name = 'ID', attribute='ID',
        widget=ForeignKeyWidget(Account,)
    )

class Meta:
     model = CourseInfoResource
    # exclude = ('','')
    