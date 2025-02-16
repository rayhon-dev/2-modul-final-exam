from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'group', 'status', 'created_at')
    list_filter = ('group', 'gender', 'status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    ordering = ('-created_at',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'slug', 'dob', 'gender', 'email', 'phone', 'photo')
        }),
        ('School Details', {
            'fields': ('group', 'grade_level', 'status', 'enrollment_date')
        }),
        ('Guardian Information', {
            'fields': ('parent_name', 'parent_phone', 'parent_email')
        }),
        ('Address', {
            'fields': ('address',)
        }),
        ('Status & Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
