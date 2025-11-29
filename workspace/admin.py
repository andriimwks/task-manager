from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    list_filter = ('created_by',)
    search_fields = ('name',)
    ordering = ('created_by',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'priority', 'completed')
    list_filter = ('project', 'completed')
    search_fields = ('name',)
    ordering = ('project', 'priority')
