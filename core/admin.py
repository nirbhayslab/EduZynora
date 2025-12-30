from django.contrib import admin
from .models import Class, Subject, Chapter, Resource

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "class_level")
    list_filter = ("class_level",)
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Chapter)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "order")
    list_filter = ("subject",)
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Resource)

class ResourceAdmin(admin.ModelAdmin):    
    list_display = ("title", "resource_type", "chapter", "order")
    list_filter = ("resource_type", "chapter")
    fieldsets = (
        (
            "Resource Identity",
            {
                "fields": ("title", "resource_type", "chapter", "order"),
            },
        ),
        (
            "Resource Content (Fill EXACTLY ONE)",
            {
                "fields": ("content", "file", "external_link"),
                "description": (
                    "Provide exactly ONE of the following: "
                    "text content, a file upload, or an external link. "
                    "Leaving all empty or filling more than one is invalid."
                ),
            },
        ),
    )
