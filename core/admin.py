from django.contrib import admin
from .models import Class, Subject, Chapter, Resource

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_level')
    list_filter = ('class_level',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    list_filter = ('subject',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'chapter')
    list_filter = ('resource_type', 'chapter')
    search_fields = ('title',)
