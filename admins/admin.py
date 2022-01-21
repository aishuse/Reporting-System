from django.contrib import admin

from .models import Course, Batch

class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'course_name', 'active_status', 'fees'
    ]
    list_filter = ('active_status', 'fees')
    search_fields = ('course_name', 'active_status')

admin.site.register(Course, CourseAdmin)

class BatchAdmin(admin.ModelAdmin):
    list_display = [
        'batch_name', 'active_status'
    ]
    list_filter = ('active_status', )
    search_fields = ('batch_name', 'active_status')

admin.site.register(Batch, BatchAdmin)