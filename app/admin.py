from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Project)
class projectModelAdmin(admin.ModelAdmin):
    list_display = ['id','category','image1','image2']

@admin.register(Products)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','typeOfProduct','description','imagebw1','imageclr2','image3','image4']