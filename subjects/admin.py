from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'credit_hours', 'status', 'grade_level', 'created_at')
    list_filter = ('status', 'grade_level', 'department', 'created_at')
    search_fields = ('name', 'department__name')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'department', 'desc', 'credit_hours')
        }),
        ('Academic Details', {
            'fields': ('status', 'grade_level', 'prerequisites')
        }),
        ('Status & Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
