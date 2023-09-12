from django.contrib import admin
from django.contrib import admin
#from .models import Course

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget
"""
# Register your models here.
class CourseAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Course
    list_display = ('ESNTL_ID', 'WLK_COURS_FLAG_NM', 'WLK_COURS_NM','COURS_DC','SIGNGU_NM','COURS_LEVEL_NM','COURS_LT_CN','COURS_DETAIL_LT_CN','ADIT_DC','COURS_TIME_CN','OPTN_DC','TOILET_DC','CVNTL_NM','LNM_ADDR','COURS_SPOT_LA','COURS_SPOT_LO')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Course, CourseAdmin)   
#admin.site.register(Course)

class CourseInfoResource(resources.ModelResource):
    WLK_COURS_FLAG_NM = fields.Field(
        column_name = 'WLK_COURS_FLAG_NM', attribute='WLK_COURS_FLAG_NM',
        widget=ForeignKeyWidget(Course,'WLK_COURS_FLAG_NM')
    )

class Meta:
     model = CourseInfoResource
    # exclude = ('','')
    """