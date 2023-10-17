from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'registration_number', 'course')
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['course'].widget.can_add_related = False
        form.base_fields['course'].widget.can_change_related = False
        return form

admin.site.register(Student, StudentAdmin)