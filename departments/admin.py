from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_head_of_department',  # To'g'rilangan
        'email',
        'phone',
        'status',
        'created_at',
        'teacher_count',
        'subject_count',
    )
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'head_of_department', 'desc', 'location')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone')
        }),
        ('Status & Metadata', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'teacher_count', 'subject_count')  # Read-only xususiyatlar

    # Method to display the head of department
    def get_head_of_department(self, obj):
        return obj.head_of_department.get_full_name() if obj.head_of_department else "No Head"
    get_head_of_department.short_description = 'Head of Department'  # Field name to be displayed in admin
