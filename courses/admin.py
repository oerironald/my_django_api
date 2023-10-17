from django.contrib import admin
from .models import Course, Subject
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('subjects',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Course,CourseAdmin)
admin.site.register(Subject, SubjectAdmin)