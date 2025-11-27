from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    list_filter = ('created_by',)
    search_fields = ('name',)
    ordering = ('created_by',)
