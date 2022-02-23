from atexit import register
from django.contrib import admin

from devices.models import *

class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'data_update', ) # поля записей
    list_display_links = ('model', 'data_update', 'brand',) # ссылки записей
    search_fields = ('model', 'brand',) # поиск по записям
    list_filter = ('brand', 'data_update', ) # фильтрация

admin.site.register(Smartphone, SmartphoneAdmin)