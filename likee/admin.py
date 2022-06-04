from django.contrib import admin
from .models import Likee


class likeeAdmin(admin.ModelAdmin):
    list_display= ['id','active']
    list_editable = ['active']


admin.site.register(Likee,likeeAdmin)