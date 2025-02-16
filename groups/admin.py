from django.contrib import admin
from .models import  Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'schedule','class_teacher', 'academic_year', 'max_students', 'status', 'created_at')
    list_filter = ('grade_level', 'schedule', 'status', 'created_at')
    search_fields = ('name', 'academic_year')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'grade_level', 'schedule', 'academic_year', 'max_students', 'desc')
        }),
        ('Relationships', {
            'fields': ('subjects', 'class_teacher')
        }),
        ('Status & Metadata', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    filter_horizontal = ('subjects',)
    readonly_fields = ('created_at', 'updated_at')