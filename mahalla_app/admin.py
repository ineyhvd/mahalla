from django.contrib import admin
from .models import Viloyat, Tuman, Mahalla

@admin.register(Viloyat)
class ViloyatAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Tuman)
class TumanAdmin(admin.ModelAdmin):
    list_display = ['name', 'viloyat']

@admin.register(Mahalla)
class MahallaAdmin(admin.ModelAdmin):
    list_display = ['name', 'tuman', 'population', 'houses']