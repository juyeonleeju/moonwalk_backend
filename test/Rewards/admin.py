

# Register your models here.
from django.contrib import admin

# Register your models here.
from.models import Reward

from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
#class RewardAdmin(admin.ModelAdmin):

class RewardAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Reward
    list_display = ('xp','User_lev')
    search_fields = ['ipa', 'dev_hostname']

admin.site.register( Reward, RewardAdmin)   


class RewardInfoResource(resources.ModelResource):
    xp = fields.Field(
        column_name = 'xp',attribute='xp',
        widget=ForeignKeyWidget(Reward,'xp')
    )
#어디서 찾아서 복붙한건데 무슨 문법인지 모르겟ㅠㅜ

class Meta:
     model = RewardInfoResource
     exclude = ('','')